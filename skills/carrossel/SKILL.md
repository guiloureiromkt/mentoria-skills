---
name: carrossel
description: Monta carrossel de Instagram premium (8-10 slides · 1080×1350) a partir de um tema, um post ou um material do cliente. A IA cuida da história, da diagramação, do HTML e do corte dos slides; a ARTE é tua, feita no Illustrator ou no Canva — esta skill não gera imagem por IA. Use quando pedir "monta um carrossel", "transforma isso em carrossel", "carrossel pro Instagram", "carrossel pro meu cliente". Não serve pra post de blog, landing page ou vídeo.
---

# Carrossel — o sistema

Transforma um tema, um texto ou um material de cliente num **carrossel de Instagram de 8 a 10 slides** (1080×1350), com história bem contada, diagramação variada e legenda pronta.

**A divisão de trabalho aqui é deliberada:** a IA faz o que ela faz bem — estruturar a história, diagramar, escrever o HTML, cortar os slides no tamanho certo. **A arte é tua.** Nada aqui gera ilustração por IA. Você desenha no Illustrator (ou monta no Canva), exporta, e o sistema encaixa. É mais trabalho seu e o resultado não parece feito por robô — que é o ponto.

## Antes da primeira vez: o arquivo da marca

Esta skill lê um arquivo chamado `marca.md` na pasta do projeto (ou do cliente). É ele que diz qual é a cara do carrossel. Se não existir, a IA pergunta e cria com você. O mínimo que ele precisa ter:

```markdown
# Marca: NOME

cores:
  base: #0B0710        # o fundo, quase sempre escuro
  acento: #E62B54      # a cor que destaca, usada com parcimônia
  claro: #F2E9D6       # o creme/branco do texto

fontes:
  titulo: Anta         # qualquer uma do Google Fonts
  corpo: ABeeZee
  numero: JetBrains Mono

assinatura:
  avatar: arte/avatar.png
  arroba: "@cliente"

voz:
  como fala: (2-3 linhas do jeito de escrever da marca)
  nunca escreve: (palavras e vícios proibidos)
```

Para um cliente de saúde, esse arquivo também carrega a linha de conformidade do conselho dele — o que precisa aparecer em toda peça (CRM e RQE para médico, nome e CRO para dentista, CRP para psicólogo). O rodapé do template já tem lugar para isso.

## Os princípios que não se quebram

1. **Zero invenção.** Nenhum número, caso, preço ou data entra no carrossel sem estar no material de origem. Na dúvida, corta o número. Vale mais um slide a menos do que um dado inventado na mão de um cliente que responde a conselho profissional.
2. **Concreto, não abstrato.** Cada conceito vira uma cena que dá pra desenhar. "Funil vazando dinheiro pelas laterais" é briefing de arte. "Crescimento sustentável" não é nada.
3. **Só a capa é full-bleed.** O miolo alterna disposições — arte embaixo, arte na metade, tipográfico puro. Carrossel inteiro cheio de imagem cansa e todos os slides viram o mesmo slide.
4. **Uma paleta por carrossel.** Trocar a cor de um slide solto no meio parece erro. Se variar, varia em bloco contíguo (dois atos), no máximo duas paletas.
5. **Não publica.** A skill entrega os PNGs e a legenda em rascunho. Publicar é decisão de quem assina.

## O fluxo, em sete passos

### 1 · Origem e extração honesta
Lê o material de origem (post, briefing, transcrição, material do cliente) e extrai três coisas: a **tese**, as **três ideias centrais** e a **lista de números e casos reais** que o texto cita. Essa lista é a única fonte de dado permitida daqui pra frente.

Se a origem é um tema livre, sem material: avisa que não vai ter número, e o carrossel se sustenta na ideia, não em estatística.

### 2 · A estrutura da história
Dez slides é o padrão (o Instagram permite até 20, mas 10 é onde o formato rende). **Um beat por slide, sem amontoar.** O arco está em `references/design-system.md`.

### 3 · Três opções de capa — e você escolhe
A IA propõe **três capas diferentes** do mesmo conceito: três ângulos, três frases de gancho, três composições. Ela recomenda uma e explica por quê, mas **espera você escolher**. A capa escolhida crava a paleta do resto.

Nesta etapa a IA entrega o **briefing de arte** de cada slide: o que desenhar, em que composição, com qual espaço vazio. É o que você leva pro Illustrator.

### 4 · Você faz a arte
Exporta em PNG e salva na pasta `arte/` do projeto, com nome que diga o slide: `capa.png`, `slide-3.png`, `slide-5.png`. Só os slides que pedem arte — os tipográficos não pedem.

A composição importa e está no briefing: arte que vai na faixa inferior precisa do assunto na metade de baixo e espaço vazio em cima; arte de meia-página precisa do assunto centralizado, porque vai ser cortada na vertical.

### 5 · Montar o HTML
A IA monta o `carrossel.html` a partir de `templates/modelo.html`, trocando texto, arte e cores pelos da `marca.md`. As classes de disposição (`cover`, `l-bottom`, `l-right`, `l-left`, `l-type`) estão explicadas no sistema de design.

### 6 · Renderizar e cortar
```bash
python scripts/render_slice.py carrossel.html slides/ 10
```
Renderiza no Chrome e corta em `slide-1.png` até `slide-10.png`, cada um 1080×1350. **Passe o número real de slides** — se errar, corta no lugar errado.

Depois, olha os slides de verdade, principalmente a capa e os de meia-página, que são os que quebram. Ajusta e roda de novo.

### 7 · Legenda e entrega
Escreve a legenda seguindo `references/legenda.md`, na voz que está na `marca.md`. Entrega os PNGs, a legenda e a linha do primeiro comentário. Não publica.

## Referências
- `references/design-system.md` — paletas, disposições, arco da história, briefing de arte. **Lê antes de montar o HTML.**
- `references/legenda.md` — estrutura e voz da legenda.
- `templates/modelo.html` — o ponto de partida, já com as cinco disposições montadas.

## O que precisa estar instalado
- **Google Chrome** (o script renderiza nele)
- **Python** com a biblioteca Pillow: `pip install pillow`

Se o Chrome estiver em lugar fora do comum, abre `scripts/render_slice.py` e acrescenta o caminho na lista da função `find_chrome()`.
