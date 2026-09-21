#!/usr/bin/env python3
"""Retro de tokens: os números do ccusage, por dia, por projeto e por sessão, sem gastar token.

Uso:
    python3 retro_tokens.py --dias 7          # resumo em texto (padrão: 7 dias)
    python3 retro_tokens.py --dias 7 --json   # o mesmo em JSON, para um loop ler
    python3 retro_tokens.py --top 15          # quantas sessões listar (padrão 10)

Lê: `npx ccusage@latest daily --json` e `session --json` (ferramenta aberta, MIT; roda sem instalar).
Para cada sessão cara, lê SÓ a primeira linha que a pessoa digitou, nos arquivos locais do Claude Code
(~/.claude/projects/<projeto>/<sessao>.jsonl), para a sessão ser reconhecível. Não manda nada para fora,
não apaga nada, não lê o resto da conversa. Sem dependências além da biblioteca padrão e do npx.
"""
import argparse
import json
import os
import subprocess
import sys
from datetime import date, datetime, timedelta
from pathlib import Path


def ccusage(*args):
    cmd = ["npx", "-y", "ccusage@latest", *args, "--json"]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=180, check=False)
    except FileNotFoundError:
        sys.exit("npx não encontrado: instale o Node.js (o ccusage roda por npx)")
    if out.returncode != 0 or not out.stdout.strip():
        sys.exit(f"ccusage falhou ({' '.join(args)}): {out.stderr.strip()[:300]}")
    return json.loads(out.stdout)


def arquivo_da_sessao(session_id):
    """O .jsonl local da sessão, se existir. O nome da pasta-mãe codifica o projeto (-home-gui-x → /home/gui/x).
    Aproximação: hífen no nome original vira barra (guios-command aparece como guios/command)."""
    base = Path.home() / ".claude" / "projects"
    if not base.is_dir():
        return None
    for f in base.glob(f"*/{session_id}.jsonl"):
        if f.is_file():
            return f
    return None


def projeto_do_arquivo(f):
    if f is None:
        return "(sem projeto)"
    nome = f.parent.name
    return "/" + nome.lstrip("-").replace("-", "/") if nome.startswith("-") else nome


def primeira_frase(session_id, project_hint=None):
    """A primeira mensagem humana da sessão, cortada em 120 caracteres. None se não achar."""
    f = arquivo_da_sessao(session_id)
    for f in ([f] if f else []):
        try:
            with f.open(encoding="utf-8", errors="replace") as fh:
                for linha in fh:
                    try:
                        d = json.loads(linha)
                    except json.JSONDecodeError:
                        continue
                    if d.get("type") != "user":
                        continue
                    msg = d.get("message", {})
                    conteudo = msg.get("content")
                    texto = None
                    if isinstance(conteudo, str):
                        texto = conteudo
                    elif isinstance(conteudo, list):
                        for parte in conteudo:
                            if isinstance(parte, dict) and parte.get("type") == "text":
                                texto = parte.get("text")
                                break
                    if texto and not texto.startswith("<"):
                        texto = " ".join(texto.split())
                        return texto[:120] + ("…" if len(texto) > 120 else "")
        except OSError:
            continue
    return None


def projeto_de(sessao):
    # o ccusage (set/2026) não traz o projeto na sessão; a pasta do .jsonl local diz
    sid = str(sessao.get("period") or sessao.get("sessionId") or "")
    return projeto_do_arquivo(arquivo_da_sessao(sid))


def ultima_atividade(sessao):
    meta = sessao.get("metadata") or {}
    for k in ("lastActivity", "lastActivityAt", "endTime", "date"):
        v = meta.get(k) or sessao.get(k)
        if v:
            return str(v)[:10]
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", type=int, default=7)
    ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    hoje = date.today()
    ini = hoje - timedelta(days=a.dias - 1)
    ini_ant = ini - timedelta(days=a.dias)

    daily = ccusage("daily").get("daily", [])
    por_dia = {}
    for r in daily:
        d = str(r.get("period") or r.get("date"))[:10]
        try:
            dd = date.fromisoformat(d)
        except ValueError:
            continue
        por_dia[dd] = {"custo": float(r.get("totalCost") or 0), "tokens": int(r.get("totalTokens") or 0)}
    semana = {d: v for d, v in por_dia.items() if ini <= d <= hoje}
    anterior = {d: v for d, v in por_dia.items() if ini_ant <= d < ini}
    soma = lambda m, k: sum(v[k] for v in m.values())

    sessoes = ccusage("session").get("session", [])
    recentes = []
    for s in sessoes:
        ult = ultima_atividade(s)
        if ult:
            try:
                if date.fromisoformat(ult) < ini:
                    continue
            except ValueError:
                pass
        recentes.append(s)
    # sem data na sessão, o ccusage já filtra pouco: ordenar por custo e cortar
    recentes.sort(key=lambda s: float(s.get("totalCost") or 0), reverse=True)

    por_projeto = {}
    for s in recentes:
        p = projeto_de(s)
        por_projeto.setdefault(p, {"custo": 0.0, "sessoes": 0})
        por_projeto[p]["custo"] += float(s.get("totalCost") or 0)
        por_projeto[p]["sessoes"] += 1
    projetos = sorted(por_projeto.items(), key=lambda kv: kv[1]["custo"], reverse=True)

    top = []
    for s in recentes[: a.top]:
        sid = str(s.get("period") or s.get("sessionId") or "")
        proj = projeto_de(s)
        hint = Path(proj).name if proj and proj != "(sem projeto)" else None
        top.append({
            "sessao": sid,
            "projeto": proj,
            "ultima_atividade": ultima_atividade(s),
            "custo": round(float(s.get("totalCost") or 0), 2),
            "tokens": int(s.get("totalTokens") or 0),
            "primeira_frase": primeira_frase(sid, hint),
        })

    resultado = {
        "periodo": {"de": ini.isoformat(), "ate": hoje.isoformat(), "dias": a.dias},
        "semana": {"custo": round(soma(semana, "custo"), 2), "tokens": soma(semana, "tokens"), "dias_com_uso": len(semana)},
        "anterior": {"custo": round(soma(anterior, "custo"), 2), "tokens": soma(anterior, "tokens"), "dias_com_uso": len(anterior)},
        "por_dia": [{"dia": d.isoformat(), **v} for d, v in sorted(semana.items())],
        "por_projeto": [{"projeto": p, "custo": round(v["custo"], 2), "sessoes": v["sessoes"]} for p, v in projetos[:10]],
        "sessoes_mais_caras": top,
        "aviso": "sessões sem data no ccusage entram na lista pelo custo, não pelo período; confira a coluna de atividade",
    }
    if a.json:
        print(json.dumps(resultado, ensure_ascii=False, indent=2))
        return

    s, an = resultado["semana"], resultado["anterior"]
    print(f"RETRO DE TOKENS · {ini} a {hoje} ({a.dias} dias)")
    print(f"  esta semana: US$ {s['custo']:.2f} · {s['tokens']:,} tokens · {s['dias_com_uso']} dias com uso")
    print(f"  anterior:    US$ {an['custo']:.2f} · {an['tokens']:,} tokens · {an['dias_com_uso']} dias com uso")
    print("\nPOR DIA")
    for r in resultado["por_dia"]:
        print(f"  {r['dia']}  US$ {r['custo']:>8.2f}  {r['tokens']:>14,}")
    print("\nPOR PROJETO (sessões com atividade no período)")
    for r in resultado["por_projeto"]:
        print(f"  US$ {r['custo']:>8.2f}  {r['sessoes']:>3} sessões  {r['projeto']}")
    print(f"\nSESSÕES MAIS CARAS (top {a.top})")
    for r in top:
        frase = r["primeira_frase"] or "(primeira frase não encontrada)"
        print(f"  US$ {r['custo']:>7.2f}  {r['ultima_atividade'] or '----------'}  {Path(r['projeto']).name if r['projeto'] != '(sem projeto)' else '(sem projeto)'}")
        print(f"           \"{frase}\"")
    print(f"\n{resultado['aviso']}")


if __name__ == "__main__":
    main()
