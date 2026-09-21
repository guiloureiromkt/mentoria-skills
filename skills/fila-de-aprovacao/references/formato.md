# O formato do pedido

Um arquivo por ação, em `aprovar/`. Nome: `AAAA-MM-DD-<verbo>-<objeto>.md`. Exemplo: `2026-10-03-pausar-conjunto-remarketing.md`.

```markdown
---
acao: pausar conjunto de anúncios
alvo: Meta · conta Garimp.ai · conjunto "remarketing 30d" (id 1203...)
proposto_por: loop-trafego · 2026-10-03 07:12
motivo: CPA de R$ 41 contra teto de R$ 25 por 3 dias seguidos (saida/relatorio-diario.md, 2026-10-01 a 03)
reversivel: sim, reativar o conjunto pelo mesmo id
dinheiro: não
prazo: 2026-10-04 18:00
---

## O que vai ser feito, exatamente
1. Pausar o conjunto "remarketing 30d" (id 1203...) na conta Garimp.ai.
2. Registrar o id e o estado anterior ("ativo") na evidência.

## O que NÃO vai ser feito
- Não mexer nos outros conjuntos da campanha.
- Não alterar verba.
```

## Os campos, um por um

| Campo | O que é | Regra |
|---|---|---|
| `acao` | o verbo e o objeto, em uma linha | um pedido, uma ação |
| `alvo` | onde, com identificador | id, url ou nome exato; "a campanha" não serve |
| `proposto_por` | quem propôs e quando | loop, agente ou pessoa · data e hora |
| `motivo` | por quê, com a origem do número | arquivo ou plataforma + data; sem impressão |
| `reversivel` | como desfazer | "sim, como" ou "não" |
| `dinheiro` | a ação paga, transfere ou reembolsa? | se sim, a execução é sempre de uma pessoa |
| `prazo` | até quando vale | passou, não executa |

## As linhas que entram depois

Quem aprova acrescenta no fim do arquivo e move para `aprovado/`:

```
aprovado_por: Eduardo · 2026-10-03 14:20
```

O executor acrescenta:

```
## Execução
executado_por: executor · 2026-10-03 14:31 · evidência: saida/evidencias/2026-10-03-pausar-conjunto-remarketing/
```

O verificador acrescenta:

```
## Verificação
verificado_por: verificador · 2026-10-03 14:34 · ok
```

ou

```
verificado_por: verificador · 2026-10-03 14:34 · divergência: o conjunto 1203 foi pausado, mas a verba do conjunto 1204 mudou de 50 para 30 (não estava no pedido) → pedido de reversão em aprovar/2026-10-03-reverter-verba-1204.md
```

Ação de dinheiro, no lugar de `executado_por`:

```
preparado_por: executor · 2026-10-05 08:00 · boleto em saida/evidencias/.../boleto.pdf, valor R$ 1.240,00 conferido com a NF 8812 · aguardando pagamento por pessoa
```
