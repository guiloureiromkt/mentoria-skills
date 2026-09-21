#!/usr/bin/env python3
"""Lista a fila de aprovação de um harness sem gastar token.

Uso, na raiz do harness (onde estão aprovar/ e aprovado/):
    python3 fila.py            # tabela
    python3 fila.py --json     # o mesmo, em JSON (para um loop ler)

Estados:
    pendente   em aprovar/, prazo ainda vale
    vencido    em aprovar/, prazo passou (fica como registro; não se executa)
    aprovado   em aprovado/, com aprovado_por, sem executado_por/preparado_por
    executado  em aprovado/, com executado_por e sem verificado_por
    preparado  em aprovado/, ação de dinheiro preparada, esperando pessoa
    concluido  em aprovado/, verificado_por presente
    invalido   arquivo sem frontmatter ou sem os campos mínimos
Sem dependências além da biblioteca padrão.
"""
import json
import re
import sys
from datetime import datetime
from pathlib import Path

CAMPOS_MINIMOS = ("acao", "alvo", "proposto_por", "motivo", "prazo")


def frontmatter(texto):
    m = re.match(r"^---\n(.*?)\n---\n", texto, re.S)
    if not m:
        return None
    campos = {}
    for linha in m.group(1).splitlines():
        if ":" in linha:
            k, v = linha.split(":", 1)
            campos[k.strip()] = v.strip()
    return campos


def linha_marcada(texto, chave):
    m = re.search(rf"^{chave}:\s*(.+)$", texto, re.M)
    return m.group(1).strip() if m else None


def parse_prazo(valor):
    if not valor:
        return None
    for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%dT%H:%M", "%Y-%m-%d"):
        try:
            return datetime.strptime(valor[: len(fmt) + 2].strip(), fmt)
        except ValueError:
            continue
    return None


def estado_de(caminho, pasta, agora):
    texto = caminho.read_text(encoding="utf-8", errors="replace")
    fm = frontmatter(texto)
    if fm is None or any(c not in fm for c in CAMPOS_MINIMOS):
        return "invalido", fm or {}, None
    prazo = parse_prazo(fm.get("prazo"))
    if pasta == "aprovar":
        if prazo and prazo < agora:
            return "vencido", fm, prazo
        return "pendente", fm, prazo
    # aprovado/
    if linha_marcada(texto, "verificado_por"):
        return "concluido", fm, prazo
    if linha_marcada(texto, "executado_por"):
        return "executado", fm, prazo
    if linha_marcada(texto, "preparado_por"):
        return "preparado", fm, prazo
    if linha_marcada(texto, "aprovado_por"):
        return "aprovado", fm, prazo
    return "invalido", fm, prazo  # em aprovado/ sem aprovado_por: alguém moveu sem assinar


def listar(raiz):
    agora = datetime.now()
    itens = []
    for pasta in ("aprovar", "aprovado"):
        d = raiz / pasta
        if not d.is_dir():
            continue
        for f in sorted(d.glob("*.md")):
            if f.name.lower() == "readme.md":
                continue
            estado, fm, prazo = estado_de(f, pasta, agora)
            dias = (prazo - agora).days if prazo else None
            itens.append({
                "arquivo": f"{pasta}/{f.name}",
                "estado": estado,
                "acao": fm.get("acao", ""),
                "alvo": fm.get("alvo", ""),
                "dinheiro": fm.get("dinheiro", ""),
                "prazo": fm.get("prazo", ""),
                "dias_ate_prazo": dias,
            })
    return itens


def main():
    raiz = Path.cwd()
    itens = listar(raiz)
    if "--json" in sys.argv:
        print(json.dumps(itens, ensure_ascii=False, indent=2))
        return
    if not itens:
        print("fila vazia (nenhum .md em aprovar/ ou aprovado/ além do README)")
        return
    ordem = ["aprovado", "executado", "preparado", "pendente", "vencido", "concluido", "invalido"]
    itens.sort(key=lambda i: (ordem.index(i["estado"]), i["arquivo"]))
    largura = max(len(i["arquivo"]) for i in itens)
    print(f"{'ESTADO':<10} {'ARQUIVO':<{largura}}  AÇÃO · ALVO · PRAZO")
    for i in itens:
        prazo = i["prazo"]
        if i["dias_ate_prazo"] is not None and i["estado"] in ("pendente", "vencido"):
            prazo += f" ({i['dias_ate_prazo']:+d}d)"
        extra = " · DINHEIRO" if str(i["dinheiro"]).lower().startswith("s") else ""
        print(f"{i['estado']:<10} {i['arquivo']:<{largura}}  {i['acao']} · {i['alvo']} · {prazo}{extra}")
    resumo = {}
    for i in itens:
        resumo[i["estado"]] = resumo.get(i["estado"], 0) + 1
    print("\n" + " · ".join(f"{k}: {v}" for k, v in resumo.items()))


if __name__ == "__main__":
    main()
