# Mentoria Skills — as ferramentas da Mão na Massa

**Skills de [Claude Code](https://claude.com/claude-code) em português, para quem está construindo o próprio estúdio.** A `mentoria:carrossel` monta o carrossel de Instagram inteiro — história, diagramação, corte dos slides — e deixa a arte com você, porque arte de IA em peça de cliente se reconhece de longe. A `mentoria:trendseeker` varre o teu mercado toda semana e devolve o que mudou, com fonte e data. Vêm acompanhadas de uma skill de design de site e de uma que acha outras skills quando você precisa.

Elas existem porque eu uso na minha operação e porque os meus mentorados precisavam delas. Não são demonstração.

---

## Instalar

São dois comandos, e existem duas formas de dar os mesmos dois. Escolhe uma.

**Dentro do Claude Code** — digita na linha onde você conversa com ele, do mesmo jeito que digita uma pergunta:

```
/plugin marketplace add guiloureiromkt/mentoria-skills
/plugin install mentoria@mentoria-skills
```

**Ou no terminal** — a mesma coisa, com a palavra `claude` na frente:

```bash
claude plugin marketplace add guiloureiromkt/mentoria-skills
claude plugin install mentoria@mentoria-skills
```

⚠️ **Não misture as duas.** O comando que começa com barra (`/plugin`) só funciona dentro do Claude Code. Se você colar ele no terminal, vai dar *"arquivo ou diretório inexistente"* — o terminal procura um programa chamado `/plugin`, que não existe.

Fecha e abre o Claude Code. Pronto — sem copiar pasta, sem baixar ZIP.

Para conferir, pergunta ao Claude: *que skills você tem disponíveis?* As quatro têm que aparecer.

Se preferir instalar na mão, ou se o `/plugin` não estiver disponível na tua versão, o caminho por cópia de pasta está em [docs/00-como-instalar.md](docs/00-como-instalar.md).

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

### 🎨 `impeccable` — design de site que não sai genérico

Cria, critica, audita e melhora página e site. É a que te tira do resultado "legalzinho mas parece template". Skill de terceiro, Apache 2.0, redistribuída aqui sem modificação.

### 🔎 `find-skills` — acha o que falta

Quando você precisa de uma skill que não está aqui, pede: *acha uma skill pra editar vídeo*. Ela procura no ecossistema aberto e instala a escolhida.

---

## As integrações

- **[Canva](docs/01-canva.md)** — conector oficial dentro do Claude. Dois minutos, sem instalar nada.
- **[Illustrator](docs/02-adobe.md)** — dá para controlar o Illustrator pelo Claude, mas a instalação é técnica de verdade. O documento explica o que vem pela frente antes de você começar.

E em **[docs/03-mais-skills.md](docs/03-mais-skills.md)**: `deep-research` (pesquisa com bibliografia), `taste` (mais repertório visual) e o meu outro marketplace, o [ultra-skills](https://github.com/guiloureiromkt/ultra-skills), que constrói site inteiro e audita SEO, GEO e medição.

---

## Licenças

`carrossel` e `trendseeker` são minhas, sob MIT — usa, muda, leva pra onde quiser.

`impeccable` é de terceiro, sob Apache 2.0, com a licença original preservada dentro da pasta. `find-skills` vem do ecossistema aberto de Agent Skills, redistribuída sem modificação.
