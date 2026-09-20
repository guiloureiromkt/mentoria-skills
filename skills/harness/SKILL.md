---
name: harness
description: Entrevista que preenche a ficha de 10 campos de um harness (ambiente fechado para um propósito só) e escreve o CLAUDE.md do harness e o intent/<nome>.md no formato do cycle. Use quando pedir "monta o harness de X", "ficha do harness", "quero fechar um ambiente pra isso", "que agentes e fontes esse projeto precisa", ou antes de rodar /cycle:init num repositório novo. Não constrói o harness, não instala skill, não cria loop. Entrega a ficha, o arquivo mãe e o intent, que são o que decide tudo depois.
---

# Harness — a ficha que vira ambiente

Um **harness** é uma pasta fechada para um propósito só: só os agentes, skills, loops, dados e pessoas daquele trabalho entram; o resto do teu segundo cérebro fica fora. É o que impede a IA de misturar a Carol do financeiro com a Carol do conteúdo, e o que permite dar acesso a outra pessoa sem entregar tudo.

Esta skill faz uma coisa: **preenche a ficha de 10 campos do harness com você, por pergunta, e escreve três arquivos** a partir dela. Ela não constrói nada. O que ela entrega é o que decide tudo que vem depois.

O par dela é o **template de harness** (`github.com/guiloureiromkt/harness-template`): o esqueleto de pastas, permissões e fila de aprovação. A ficha diz o que vai dentro; o template é a caixa.

## Os princípios que não se quebram

1. **Uma pergunta por vez, com a resposta recomendada.** Quem responde decide; a skill sugere e explica em uma linha por quê. Nunca duas perguntas na mesma mensagem.
2. **Fato não se pergunta, se olha.** Se a resposta está no repositório, nos loops que já existem, no `marca.md` ou num arquivo que a pessoa citou, a skill lê e confirma ("vi que existem quatro loops de tráfego, são estes?") em vez de pedir de novo.
3. **Um harness, um propósito.** Se a ficha começa a ter dois públicos, duas marcas ou dois tipos de dado sigiloso, a skill para e diz: são dois harnesses. E oferece preencher o segundo depois.
4. **O que não cabe fica nomeado.** Toda função que a pessoa quer e não entra neste harness vai para uma lista "fica fora, e onde mora", para não sumir como o módulo 8 do Eduardo sumiu.
5. **Zero invenção.** Conector, API, custo e licença entram na ficha só com o que a pessoa sabe ou com o que a skill conferiu. "Não sei ainda" é resposta válida e fica escrito assim.

## Antes de começar: onde estamos

Olha a pasta atual e responde para si mesma, sem perguntar:
- É um repositório clonado do template? (tem `aprovar/`, `saida/`, `skills-permitidas/`). Se sim, os arquivos de saída vão aqui.
- Não é? Então a skill escreve a ficha e o intent numa pasta `harness-<nome>/` ao lado, e diz no fim como clonar o template.
- Já existe um `CLAUDE.md` preenchido? Lê e trata como respostas dadas. Só pergunta o que falta.
- Existem loops, workflows (`.github/workflows/*.yml`), skills ou um `marca.md` por perto? Lista o que achou: vai virar resposta do campo 3 e do campo 5.

## A entrevista: os dez campos, na ordem

Cada campo tem a pergunta, a resposta recomendada quando dá para deduzir, e o que a resposta destrava. A ficha completa com exemplos está em `references/ficha.md`; lê antes da primeira rodada.

| # | Campo | O que está decidindo |
|---|---|---|
| 1 | **Propósito** | o que faz, para quem, e o que nunca faz. É a frase que abre o `CLAUDE.md` |
| 2 | **Método** | onde entra o ciclo e o graph; quais portões (dinheiro · permissão · dado destrutivo · superfície de usuário) |
| 3 | **Peças** | o que vira template, skill, loop e agente, pela régua de maturidade (3 vezes na mão → skill · 3 vezes sem correção → loop · precisa não ver o resto ou confere outro → agente) |
| 4 | **Comprar ou construir** | o que existe pronto e passa nos 4 gates (serve · licença comercial · não inunda · não roda código obscuro); o que é seu |
| 5 | **Fontes** | arquivo no repositório · plataforma por API · outro harness (só a pasta `saida/` dele) |
| 6 | **APIs e conectores** | quais são necessários e quais têm caminho grátis |
| 7 | **Interface** | chat na pasta · pasta de aprovação · portal com MCP. A maioria nunca sai do primeiro |
| 8 | **Hospedagem** | repositório · Actions · máquina · VPS · Drive |
| 9 | **Acesso e permissão** | quem entra, o que pode, o que é bloqueado, nas três camadas (repositório · Claude · mundo) |
| 10 | **Custo e operação** | de quem é o token em cada uso; rotina diária e semanal; o que espera aprovação |

A ordem importa: o propósito (1) decide as peças (3); as peças decidem as fontes (5); as fontes decidem os conectores (6); quem trabalha dentro (9) decide a interface (7) e o custo (10). Se uma resposta muda uma anterior, a skill volta e reescreve, dizendo o quê.

**Perguntas que a skill sempre faz, mesmo que pareçam óbvias:**
- "Quem, além de você, trabalha dentro?" (se a resposta é "ninguém", a interface é chat e o custo é a tua assinatura; se tem alguém, tem cadeira, permissão e teste de alcance)
- "Qual ação deste harness sai para o mundo?" (subir campanha, publicar, enviar, pagar). Cada uma vira um item da fila de aprovação
- "O que este harness lê que não pode vazar para outro?" (é isso que define o que fica em `saida/` e o que não sai daqui)

## O que a skill escreve no fim

Três arquivos, nesta ordem, cada um mostrado antes de gravar:

1. **`FICHA.md`**: a tabela dos dez campos preenchida, mais a lista "fica fora, e onde mora". É o documento que se leva para a aula ou para o sócio.
2. **`CLAUDE.md`**: o arquivo mãe do harness, no formato do template (`Quem lê este arquivo` · Propósito · Marca · Quem trabalha dentro · Fontes · Skills permitidas · Peças · Fila de aprovação · Custo · O que nunca faz). Se já existe um `CLAUDE.md` do template com campos `< >`, a skill preenche os campos e não toca no resto.
3. **`intent/<nome>.md`**: o intent no formato do cycle (template em `references/intent.md`, títulos em inglês como o plugin espera; o conteúdo na língua de quem respondeu), com `status: draft`. Quem aceita é a pessoa, com `/cycle:intent`, não a skill.

E uma mensagem final curta: o que foi escrito (caminhos absolutos), o que ficou como "não sei ainda", e o próximo passo (`/cycle:init` nesta pasta, ou clonar o template se ainda não clonou).

## O que esta skill não faz

- Não instala skill, não cria loop, não escreve workflow. Isso é construção, e construção passa pelo ciclo.
- Não decide por você. Recomenda, explica, espera.
- Não roda em pasta de workspace. Se a pasta atual é a raiz de tudo (tem vários projetos embaixo), a skill avisa e pede para criar ou entrar na pasta do harness.
