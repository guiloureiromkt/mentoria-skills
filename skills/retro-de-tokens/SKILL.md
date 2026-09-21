---
name: retro-de-tokens
description: Retro semanal do uso do Claude Code. Lê os números do ccusage (custo e tokens por dia, por projeto e por sessão), acha o que se repetiu na semana e propõe o que virar skill, template ou loop, com a economia estimada. Sai um relatório de uma página. Use quando pedir "retro de tokens", "onde estou gastando", "o que se repete no meu uso", "o que vale virar skill", ou como rotina de sexta. Não muda nada, não cria skill, não apaga sessão. Só mede e propõe.
---

# Retro de tokens — o que se repete vale virar skill

A pergunta desta skill não é "quanto gastei". É **"o que eu fiz três vezes na semana, na mão, que podia ser uma skill de uma linha?"** O gasto é o sintoma; a repetição é a causa. A lição que a origina é de uma mentoria de julho: amostra semanal, não diária, porque no dia a dia tudo parece único e na semana o padrão aparece.

Ela roda em três passos, e o primeiro não gasta token.

## Antes da primeira vez

Precisa do `ccusage`, ferramenta aberta (MIT) que lê os arquivos que o Claude Code já guarda na sua máquina e soma tokens e custo. Não instala nada permanente: `npx ccusage@latest` baixa e roda. Na primeira vez, o download leva um minuto.

## Passo 1 · Os números (script, sem token)

```
python3 <caminho-da-skill>/scripts/retro_tokens.py --dias 7
```

Sai um resumo em texto: custo e tokens da semana contra a semana anterior; por dia; por projeto (pasta em que a sessão rodou); as 10 sessões mais caras, cada uma com a primeira frase que você digitou nela (lida do histórico local, só a primeira linha, para você reconhecer a sessão). `--json` devolve o mesmo para um loop ler.

O que o script não faz: não lê o conteúdo das conversas além da primeira frase, não manda nada para fora, não apaga nada.

## Passo 2 · O que se repete (a skill lê o resumo)

Com o resumo na mão, a skill procura três coisas, nesta ordem:

1. **Sessões com a mesma primeira frase, ou quase.** "Atualiza a planilha do financeiro com…" três vezes na semana é uma skill esperando nome. Critério: 3 ou mais na semana, ou 2 na semana e 2 na anterior.
2. **Um projeto que custou mais do que o esperado pelo que produziu.** A pergunta é "o que saiu dali?"; se a resposta é "conversa", o custo é contexto relido (cache) e o remédio é um arquivo de contexto (CLAUDE.md da pasta, um `marca.md`, uma nota de estado) que evita reexplicar.
3. **Sessões longas de um assunto só.** Sessão de 200 mil tokens em que a última hora foi corrigir a mesma coisa é sinal de que faltou um teste ou um exemplo no prompt.

Para cada achado, a skill escreve uma linha: **o que se repetiu · quantas vezes · quanto custou no total · o que vira** (skill, template, CLAUDE.md da pasta, loop) · **a economia estimada** (custo das repetições menos o custo de uma rodada com a skill, que ela estima como a menor das repetições).

## Passo 3 · O relatório (uma página)

`saida/retro-tokens/AAAA-SS.md` (ano e semana), com:

- **Os números:** semana × semana anterior, em custo e em tokens; os três projetos mais caros.
- **O que se repetiu:** a tabela do passo 2, no máximo 5 linhas. Menos é melhor: a primeira da lista é a que vale fazer esta semana.
- **Uma proposta só:** qual repetição virar skill agora, com o nome sugerido e as três frases que ela teria que saber fazer. Se não houver repetição que valha, o relatório diz "nada a transformar esta semana" e para. Relatório sem proposta é resultado válido.
- **O que não dá para ver por aqui:** sessões no app do Claude (não passam pelo Claude Code), rotinas na nuvem, e o que outras pessoas gastam. O `ccusage` só vê esta máquina.

## Os princípios que não se quebram

1. **Mede antes de opinar.** Nenhuma linha do relatório sem número do passo 1.
2. **Propõe, não cria.** Criar a skill é decisão de quem lê, e é outra sessão.
3. **Uma proposta por semana.** Quatro propostas é lista de desejos; uma é tarefa.
4. **A economia é estimativa e diz que é.** "≈ US$ 12/semana, se a skill acertar de primeira" e não "economiza US$ 12".
5. **Privacidade:** o relatório cita a primeira frase das sessões só quando ela não tem dado de cliente; se tem, cita o projeto e a data.

## O que esta skill não faz

- Não troca modelo, não muda configuração, não sugere "usar menos". O objetivo é gastar melhor, e às vezes gastar melhor é gastar mais numa skill que acerta.
- Não avalia qualidade do que saiu das sessões. Isso é retro de trabalho, não de tokens.
- Não roda em cima de outra pessoa. Uma máquina, um dono.
