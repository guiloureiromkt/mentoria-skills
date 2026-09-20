# O intent no formato do cycle

A skill escreve `intent/<nome>.md` com estes títulos, em inglês (é o que o plugin `cycle` lê). O conteúdo vai na língua de quem respondeu. `status` fica `draft`: quem aceita é a pessoa, com `/cycle:intent`.

```markdown
---
type: intent
status: draft            # draft → accepted → closed
author: <nome (área)>
date: <AAAA-MM-DD>
origin: person
accepted_by:
---

# Intent: <nome do harness, nas palavras de quem pediu>

## Problem
<o que não dá para fazer hoje · quem sofre · o que custa, com número se houver. Vem do campo 1 e das dores ditas na entrevista>

## Proposed outcome
<como fica melhor, nas palavras de quem pediu. Não é solução técnica. Vem do campo 1>

## Sub-intents (what orbits this request)
- <cada ação para fora (campo 10) e cada pessoa dentro (campo 9) vira uma frente que não pode ser esquecida>
- <a lista "fica fora, e onde mora" entra aqui como o que NÃO é deste intent>

## What already exists (clone or learn before inventing)
| What | Where | Solves | Verdict |
|---|---|---|---|
| <campo 4: o que está pronto, com licença conferida> | <link ou caminho> | <o que resolve> | use · adapt · discard |
| <campo 3: loops e skills que já existem e vão morar aqui> | | | |

## Affected users and systems
<campo 9 (quem) + campo 5 (fontes) + campo 6 (conectores)>

## Constraints
<campo 10 (custo, teto, quem paga) · campo 9 (o que é bloqueado) · o que este harness nunca faz>

## Open questions
- <tudo que ficou como "não sei ainda" na ficha, uma por linha>
```
