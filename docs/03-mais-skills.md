# As outras skills

Estas não moram neste repositório porque têm casa própria — e instalando da casa delas você recebe as atualizações do autor. São um comando cada.

## deep-research — pesquisa profunda com fonte

Faz pesquisa de verdade: varre muitas fontes, separa o que é fato do que é opinião de blog, e escreve um relatório com citação e bibliografia. É a que você usa antes de uma reunião de posicionamento, para chegar sabendo do mercado do cliente em vez de chegar achando.

```bash
git clone https://github.com/199-biotechnologies/claude-deep-research-skill.git ~/.claude/skills/deep-research
```

No Windows (PowerShell):
```powershell
git clone https://github.com/199-biotechnologies/claude-deep-research-skill.git $HOME\.claude\skills\deep-research
```

Depois é só pedir: "faz uma pesquisa profunda sobre o mercado de odontopediatria em Uberlândia".

## taste — outro repertório visual

Onze variações de estilo (brutalista, minimalista, soft, redesenho de página existente, imagem virando código). Serve quando o resultado saiu "legalzinho mas genérico" e você quer empurrar para outro lugar.

```bash
git clone https://github.com/Leonxlnx/taste-skill.git ~/.claude/skills/taste
```

## As minhas, do marketplace

Estas são as que eu mantenho. Instalam de uma vez, como pacote, dentro do Claude Code:

```
/plugin marketplace add guiloureiromkt/ultra-skills
```

Vem junto:

- **site** — constrói site inteiro, do zero ao publicado
- **auditoria** — audita um site pronto: SEO, medição, formulário que finge enviar, código
- **humanizer** — tira a cara de texto de robô de qualquer peça
- **linkedin** — motor de conteúdo de LinkedIn na tua voz
- **diagnostico**, **deck**, **newsletter**

Depois de adicionar o marketplace, o Claude Code mostra o que tem e você escolhe o que instalar.

## E se você precisar de uma que não existe aqui

É pra isso que serve a `find-skills`, que já veio instalada:

```
acha uma skill pra editar vídeo
```

Ela procura no ecossistema aberto, te mostra as opções e instala a que você escolher.
