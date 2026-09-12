---
name: trendseeker
description: Varredura semanal do que está se mexendo no teu mercado — o que mudou de regra, o que apareceu de ferramenta, o que o concorrente começou a fazer, que dor nova o teu cliente está sentindo. Devolve uma lista curta de sinais com fonte e data, filtrada por sete lentes, num arquivo que vira pauta de conteúdo e assunto de reunião. Use quando pedir "roda o trendseeker", "o que tem de novo no mercado", "varredura da semana", "o que mudou no meu setor". Não escreve conteúdo — só traz o sinal.
---

# Trendseeker — a varredura do mercado

Esta skill olha **para fora**. Ela não escreve post, não valida tese, não decide nada. Ela varre fontes, aplica um filtro e devolve uma lista curta do que mudou, com link e data. O que fazer com cada sinal é decisão sua depois.

A diretriz que organiza tudo: **procurar o que desloca, não o que confirma.** Sinal que só repete o que você já acha não serve. O que vale é o que obriga a mudar de ideia, a avisar um cliente, ou a mexer num preço.

## Antes da primeira vez: o arquivo do teu mercado

A skill lê `mercado.md` na pasta onde ela roda. Se não existir, ela te entrevista e cria. O conteúdo:

```markdown
# Meu mercado

o que eu vendo: (uma linha)
pra quem: (os nichos que você atende, com nome)
quem mais vende pra eles: (concorrentes diretos e indiretos que você conhece)

categorias que me interessam:
  - (ex: regra de publicidade dos conselhos profissionais)
  - (ex: ferramentas de design e IA)
  - (ex: comportamento de quem compra design)
  - (ex: preço e empacotamento no mercado)

fontes que eu já sigo:
  - (perfis, sites, newsletters)

o que eu NÃO quero ver:
  - (assuntos que só geram ruído pra você)
```

Para quem atende profissional de saúde, uma categoria é obrigatória: **mudança de norma dos conselhos** (CFM, CFO, CFP, OAB). É o assunto que muda o trabalho de um cliente da noite para o dia e que quase ninguém acompanha.

## Como rodar

**Varredura da semana** (o padrão, 15 a 25 minutos):
```
roda o trendseeker
```

**Foco numa categoria:**
```
roda o trendseeker só em regra de conselho
```

**Rápida** (5 a 8 sinais, 5 minutos):
```
trendseeker rápido
```

## O que a skill faz por dentro

**1 · Carrega o contexto.** Lê `mercado.md` e o arquivo de saída anterior (para não repetir sinal que você já viu).

**2 · Varre.** Busca em paralelo, por categoria, priorizando **fonte primária**: site de conselho profissional, texto de norma, imprensa setorial, relatório com metodologia. Blog de agência entra por último e é marcado como tal.

**3 · Extrai sinais crus.** Cada sinal é uma linha: o que aconteceu, onde, quando. Sem interpretação ainda.

**4 · Filtra pelas sete lentes.** Cada sinal passa pelas lentes de `references/lentes.md` e recebe nota. Sinal que não pontua em lente nenhuma é descartado — é notícia, não sinal.

**5 · Checa a data.** Sinal sem data verificável não entra. "Recentemente" não é data. Notícia requentada de 2023 apresentada como novidade é o erro mais comum das buscas.

**6 · Tira o repetido.** Compara com as varreduras anteriores.

**7 · Ranqueia e corta.** Devolve de 8 a 15 sinais, os mais deslocantes primeiro.

**8 · Mostra antes de gravar.** Apresenta a lista, você aprova ou corta, e só então ela grava o arquivo.

## O formato de cada sinal

```
#0142 · 2026-09-12 · [regra-de-conselho]
O CFO liberou dentista a participar de cartão de desconto (Res. 271/2025), mas
anunciar o valor do desconto continua proibido.
fonte: cfo.org.br · publicado 18/06/2025 · primária
lentes: dor-que-já-existe 5 · o-que-o-mercado-finge-não-ver 4
serve pra: avisar os dois clientes de odonto · vira carrossel
```

## As regras que não se quebram

1. **Data verificada ou o sinal não entra.** Sem exceção.
2. **Fonte primária sempre que existir.** Se a notícia é sobre uma resolução, a fonte é a resolução, não o blog que comentou.
3. **Não inventa sinal.** Se a varredura veio fraca, a resposta é "a semana veio fraca", com os três sinais que prestaram. Lista cheia de enchimento é pior que lista curta.
4. **Não escreve o conteúdo.** A skill para no sinal. Transformar em carrossel é outro trabalho, com outra skill.
5. **Mostra antes de gravar.** Nada entra no arquivo sem você ver.

## Referências
- `references/lentes.md` — as sete lentes, com a pergunta de cada uma e como pontuar
- `references/fontes.md` — como montar e manter o banco de fontes
