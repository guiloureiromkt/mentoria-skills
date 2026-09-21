# Mentoria Skills — as ferramentas da Mão na Massa

**Skills de [Claude Code](https://claude.com/claude-code) em português, para quem está construindo o próprio estúdio.** A `mentoria:carrossel` monta o carrossel de Instagram inteiro — história, diagramação, corte dos slides — e deixa a arte com você, porque arte de IA em peça de cliente se reconhece de longe. A `mentoria:trendseeker` varre o teu mercado toda semana e devolve o que mudou, com fonte e data. Vêm acompanhadas de uma skill de design de site e de uma que acha outras skills quando você precisa.

Elas existem porque eu uso na minha operação e porque os meus mentorados precisavam delas. Não são demonstração.

---

## Instalar

São cinco marketplaces e um comando de instalação. O último puxa os outros quatro sozinho, então a ordem importa: adiciona os cinco primeiro, instala por último.

**Dentro do Claude Code** (digita na linha onde você conversa com ele, um de cada vez):

```
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
/plugin marketplace add Leonxlnx/taste-skill
/plugin marketplace add anthropics/skills
/plugin marketplace add zarazhangrui/frontend-slides
/plugin marketplace add guiloureiromkt/mentoria-skills
/plugin install mentoria@mentoria-skills
```

**Ou no terminal, numa linha só** (copia e cola inteiro):

```bash
claude plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill && claude plugin marketplace add Leonxlnx/taste-skill && claude plugin marketplace add anthropics/skills && claude plugin marketplace add zarazhangrui/frontend-slides && claude plugin marketplace add guiloureiromkt/mentoria-skills && claude plugin install mentoria@mentoria-skills -y
```

No fim, a mensagem tem que dizer `Successfully installed plugin: mentoria@mentoria-skills (+ 4 dependencies)`.

⚠️ **Não misture os dois.** Comando que começa com barra (`/plugin`) só funciona dentro do Claude Code. Colado no terminal, devolve *"arquivo ou diretório inexistente"*.

Fecha e abre o Claude Code, e pergunta: *que skills você tem disponíveis?*

---

## O que cada uma faz

### 🎠 `mentoria:carrossel` — a arte é tua

O jeito comum de fazer carrossel com IA é pedir a imagem para a IA. O resultado tem cara de IA, e quem contrata design percebe.

Aqui a divisão é outra: a IA faz o que ela faz bem — estrutura a história em dez beats, escolhe as disposições para nenhum slide parecer o anterior, monta o HTML, renderiza e corta tudo em 1080×1350 no tamanho exato do Instagram. **Você faz a arte**, no Illustrator ou onde quiser, e ela encaixa.

Ela também propõe **três capas** e espera você escolher, entrega o **briefing de arte** de cada slide (o que desenhar, em que composição, com qual espaço vazio) e escreve a legenda na voz da marca. Não publica nada: entrega em rascunho.

Precisa de um `marca.md` na pasta do projeto, com cores, fontes e voz. Se não existir, ela entrevista você e cria.

### 📡 `mentoria:trendseeker` — o que mudou no teu mercado

Uma varredura por semana, com uma diretriz: **procurar o que desloca, não o que confirma.**

Ela busca priorizando fonte primária, filtra cada sinal por sete lentes, **descarta o que não tem data verificável** — o erro mais comum das buscas é notícia de dois anos atrás vestida de novidade — e devolve de 8 a 15 sinais com link, data e para que servem.

Para quem atende profissão regulamentada, ela vigia o que quase ninguém acompanha: mudança de norma dos conselhos. Uma linha numa resolução reescreve como uma categoria inteira comunica.

### 🧱 `mentoria:harness` — a ficha que fecha um ambiente

Um **harness** é uma pasta fechada para um propósito só: só os agentes, skills, loops, dados e pessoas daquele trabalho entram; o resto do teu segundo cérebro fica fora. É o que impede a IA de misturar a Carol do financeiro com a Carol do conteúdo, e o que permite dar acesso a outra pessoa sem entregar tudo.

Esta skill **entrevista você pelos dez campos da ficha** (propósito, método, peças, comprar ou construir, fontes, conectores, interface, hospedagem, acesso, custo) e escreve três arquivos: a ficha, o `CLAUDE.md` do harness e o `intent/` no formato do cycle. Uma pergunta por vez, com a resposta recomendada. Fato ela não pergunta: olha os loops e arquivos que já existem e confirma.

Ela não constrói nada. O par dela é o [template de harness](https://github.com/guiloureiromkt/harness-template): o esqueleto de pastas, permissões e fila de aprovação. A ficha diz o que vai dentro; o template é a caixa.

### ✅ `mentoria:fila-de-aprovacao` — o loop propõe, você aprova, outro confere

Um loop que age sozinho no mundo não merece confiança; um loop que para e espera você na frente do computador não roda de madrugada. A fila fica no meio, e é só arquivo: **o loop escreve o pedido em `aprovar/`** (ação, alvo, motivo com o número de origem, se é reversível, prazo); **você aprova movendo para `aprovado/`** com seu nome e a data, pelo GitHub, pelo Drive ou pelo Obsidian; **a skill executa só o que está aprovado**, exatamente como está escrito, guarda a evidência, e **chama um verificador em contexto separado** para conferir que o feito é o aprovado. Prazo vencido não executa. Dinheiro nunca é automático: ela prepara e para.

Vem com `scripts/fila.py`, que lista a fila (pendente, vencido, aprovado, executado, concluído) sem gastar token. É a peça que o [template de harness](https://github.com/guiloureiromkt/harness-template) já espera nas pastas `aprovar/` e `aprovado/`.

### 📉 `mentoria:retro-de-tokens` — o que se repete vale virar skill

A pergunta não é "quanto gastei", é **"o que eu fiz três vezes na semana, na mão, que podia ser uma skill de uma linha?"**. O script lê o [ccusage](https://github.com/ryoppippi/ccusage) (ferramenta aberta que soma o uso do Claude Code na tua máquina) e devolve, sem gastar token: a semana contra a anterior, por dia, por projeto, e as sessões mais caras com a primeira frase que você digitou em cada uma. A skill lê isso, acha o que se repetiu, e propõe **uma** coisa para virar skill, template ou arquivo de contexto, com a economia estimada. Relatório de uma página, uma vez por semana. Não muda nada, não apaga nada, não manda nada para fora.

### 🎨 `impeccable` — design de site que não sai genérico

Cria, critica, audita e melhora página e site. É a que te tira do resultado "legalzinho mas parece template". Skill de terceiro, Apache 2.0, redistribuída aqui sem modificação.

### 🎯 As de design que vêm junto (as dependências)

Instalam com o mesmo comando, e cada uma tem dono próprio:

- **`ui-ux-pro-max`** ([nextlevelbuilder](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill), MIT) — banco de 67 estilos de interface, 161 paletas, 57 pares de fonte e 99 diretrizes de UX, com checagem de contraste, área de toque e acessibilidade. É a mais completa do pacote pra decisão visual.
- **`taste`** ([Leonxlnx](https://github.com/Leonxlnx/taste-skill), MIT) — onze recortes de estilo: brutalista, minimalista, soft, redesenho de página existente, imagem virando código. É a que você chama quando o resultado saiu correto e sem graça.
- **`frontend-design`** (Anthropic, Apache 2.0) — interfaces de produção sem cara de template. Vem dentro do `example-skills`, que traz junto `brand-guidelines`, `canvas-design`, `theme-factory` e `webapp-testing`.
- **`frontend-slides`** ([zarazhangrui](https://github.com/zarazhangrui/frontend-slides), MIT) — apresentação em HTML com animação, do zero ou convertendo um PowerPoint que você já tem. Zero dependência: um arquivo só que abre no navegador.

### 🔎 `find-skills` — acha o que falta

Quando você precisa de uma skill que não está aqui, pede: *acha uma skill pra editar vídeo*. Ela procura no ecossistema aberto (o índice em [skills.sh](https://www.skills.sh)) e instala a escolhida.

É da **Vercel Labs**, sob MIT, copiada sem modificação — origem e licença em [skills/find-skills/ORIGEM.md](skills/find-skills/ORIGEM.md).

---

## As integrações

- **[Canva](docs/01-canva.md)** — conector oficial dentro do Claude. Dois minutos, sem instalar nada.
- **[Illustrator](docs/02-adobe.md)** — dá para controlar o Illustrator pelo Claude, mas a instalação é técnica de verdade. O documento explica o que vem pela frente antes de você começar.

E em **[docs/03-mais-skills.md](docs/03-mais-skills.md)**: `deep-research` (pesquisa com bibliografia), `taste` (mais repertório visual) e o meu outro marketplace, o [ultra-skills](https://github.com/guiloureiromkt/ultra-skills), que constrói site inteiro e audita SEO, GEO e medição.

---

## Licenças

`carrossel` e `trendseeker` são minhas, sob MIT — usa, muda, leva pra onde quiser.

`impeccable` é de terceiro, sob Apache 2.0, com a licença original preservada dentro da pasta.

`find-skills` é da [Vercel Labs](https://github.com/vercel-labs/skills), sob MIT, redistribuída sem modificação, com a licença original e a nota de origem dentro da pasta.
