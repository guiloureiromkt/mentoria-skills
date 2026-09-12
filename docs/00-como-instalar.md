# Como instalar as skills

## O jeito mais fácil: pelo Claude Code

Digita estes dois **na linha onde você conversa com o Claude**, igual a qualquer pergunta:

```
/plugin marketplace add guiloureiromkt/mentoria-skills
/plugin install mentoria@mentoria-skills
```

Fecha e abre o Claude Code. Acabou — sem baixar nada na mão.

### ⚠️ O tropeço mais comum

Comando que começa com **barra** (`/plugin`) só existe **dentro do Claude Code**. Colado no terminal, ele devolve *"arquivo ou diretório inexistente"*, porque o terminal sai procurando um programa chamado `/plugin`.

Se você prefere o terminal, os mesmos dois comandos existem lá, com a palavra `claude` na frente:

```bash
claude plugin marketplace add guiloureiromkt/mentoria-skills
claude plugin install mentoria@mentoria-skills
```

Um ou outro. Nunca os dois.

Para conferir, pergunta: *que skills você tem disponíveis?* As quatro precisam aparecer: `carrossel`, `trendseeker`, `impeccable`, `find-skills`.

---

## O jeito manual (se o `/plugin` não existir na tua versão)

Skill é uma pasta com instruções que o Claude lê quando o assunto aparece. Instalar é copiar a pasta para o lugar certo. Não tem instalador, não tem botão: é cópia de pasta.

O lugar certo é `~/.claude/skills/` — no Windows, `C:\Users\SEU-USUARIO\.claude\skills\`.

## O caminho mais curto (um comando)

Abre o terminal e cola:

**Mac ou Linux**
```bash
git clone https://github.com/guiloureiromkt/mentoria-skills.git ~/mentoria-skills && bash ~/mentoria-skills/instalar.sh
```

**Windows (PowerShell)**
```powershell
git clone https://github.com/guiloureiromkt/mentoria-skills.git $HOME\mentoria-skills; & $HOME\mentoria-skills\instalar.ps1
```

Pronto. O script copia cada skill para dentro de `~/.claude/skills/` e lista o que copiou.

## Se preferir fazer na mão

Baixa o repositório (botão verde **Code → Download ZIP**), descompacta, e arrasta cada pasta de dentro de `skills/` para dentro de `.claude/skills/` na tua pasta de usuário. É isso.

A pasta `.claude` começa com ponto e por isso fica escondida. No Windows, marca "Itens ocultos" na aba Exibir do Explorador. No Mac, aperta `Cmd + Shift + .` no Finder.

## Como saber se funcionou

Fecha e abre o Claude Code. Digita:

```
que skills você tem disponíveis?
```

As quatro precisam aparecer: `carrossel`, `trendseeker`, `impeccable`, `find-skills`.

Se não aparecerem, quase sempre é um destes dois: a pasta foi parar num nível errado (tem que ser `.claude/skills/carrossel/SKILL.md`, sem pasta a mais no meio), ou o Claude não foi reiniciado.

## Como atualizar depois

Quando eu mexer em alguma skill, você roda de novo:

```bash
cd ~/mentoria-skills && git pull && bash instalar.sh
```

No Windows, `git pull` e depois `.\instalar.ps1`.

## O que cada uma faz

| Skill | Pra que serve |
|---|---|
| `carrossel` | Monta carrossel de Instagram de 8 a 10 slides a partir de um tema ou material. A arte é tua, feita no Illustrator — a skill cuida de história, diagramação e corte |
| `trendseeker` | Varre o mercado uma vez por semana e devolve o que mudou, com fonte e data |
| `impeccable` | Design de site e de página: cria, critica, audita e melhora. É a que te salva do visual genérico |
| `find-skills` | Acha e instala outras skills quando você precisa de uma que não tem |

As outras duas que combinamos (`deep-research` e as de design que não moram aqui) estão em [03-mais-skills.md](03-mais-skills.md).
