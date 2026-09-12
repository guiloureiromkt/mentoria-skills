# Sistema de design do carrossel

Este arquivo é a parte que não muda de cliente para cliente: como o carrossel é diagramado, como a história é construída, e como a arte precisa ser composta para caber. As cores, as fontes e a voz vêm da `marca.md` de cada projeto.

## Fontes

O template carrega do Google Fonts. Os nomes abaixo são o padrão; troca pelos da marca no `marca.md`.

- **Título:** uma geométrica de caixa alta com espaçamento apertado (padrão: `Anta`)
- **Rótulo, número do slide:** uma monoespaçada (padrão: `JetBrains Mono`)
- **Corpo:** uma humanista legível em corpo pequeno (padrão: `ABeeZee`)

```html
<link href="https://fonts.googleapis.com/css2?family=Anta&family=ABeeZee:ital@0;1&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
```

Fonte de marca que não está no Google Fonts: converte para webfont e referencia local no template.

## Paleta

Três cores bastam, e é assim que elas trabalham:

| Papel | O que faz | Onde aparece |
|---|---|---|
| **Base** | o fundo, quase sempre escuro | todo slide |
| **Acento** | a cor que destaca | régua, palavra-chave, número, borda do avatar |
| **Claro** | o creme ou branco do texto | títulos e corpo |

**A regra que evita o erro mais comum:** nunca troque a paleta de um slide solto no meio. Um slide de cor diferente entre nove iguais parece defeito, não intenção. Se for variar, varia em **bloco contíguo** — por exemplo, slides 1 a 5 no problema com uma paleta e 6 a 10 na solução com outra. Duas paletas no máximo, cada uma cobrindo um trecho inteiro.

O default seguro, e o que quase sempre fica melhor: **uma paleta só no carrossel inteiro**.

## As cinco disposições

Só a capa ocupa a tela toda. O resto alterna, e é a alternância que segura a pessoa deslizando.

| Classe | Como fica | Quando usar |
|---|---|---|
| `cover` | arte ocupando tudo, gancho por cima de um degradê escuro | só a capa |
| `l-bottom` | texto em cima, régua de acento, arte na faixa de baixo | o problema, os casos |
| `l-right` | texto à esquerda, arte na metade direita | a virada, o insight |
| `l-left` | arte na metade esquerda, texto à direita | o teste, a aplicação |
| `l-type` | tipografia pura, sem arte — só texto grande e acento | contraste, transição, chamada final |

**Não repita a mesma disposição em sequência.** E não deixe três slides de texto puro seguidos nem três de arte seguidos.

Na capa, o degradê escuro vai do topo até um pouco abaixo do título — forte em cima, revelando a arte no meio e embaixo. Assim o título fica legível e a ilustração aparece.

## A assinatura

Canto superior esquerdo de todo slide: o avatar (selo redondo com borda na cor de acento) e o arroba. Canto superior direito: o número do slide, no formato `03 / 10`.

Quando o cliente é de profissão regulamentada, o rodapé do template carrega a linha de identificação exigida pelo conselho. Ela fica em corpo pequeno, na cor clara com opacidade reduzida — presente, sem competir com a mensagem.

## O arco da história

Dez slides é o padrão. Um beat por slide. A progressão vai de tensão a resolução:

1. **Capa** — o gancho que faz parar o dedo (`cover`)
2. **A cena** — a crença comum que a pessoa carrega (`l-type` ou `l-bottom`)
3. **O problema de verdade** — por que aquilo falha (`l-bottom`, com arte)
4. **A nuance** — a armadilha que quase ninguém enxerga (`l-type` ou meia-página)
5. **A evidência** — o número ou caso real que prova (`l-left`, com arte)
6. **A virada** — "mas o furo maior é…", reenquadra o problema (`l-type`)
7. **O insight central** — a tese que resolve (`l-right`, com arte)
8. **A alavanca** — o que muda de verdade na prática (`l-bottom` ou `l-type`)
9. **O teste** — a pergunta que dói, e como aplicar (`l-left`, com arte)
10. **Fecho** — a frase que fica, e a ação: salva, segue, link no primeiro comentário (`l-type`)

Adapta os beats ao tema, mantendo a progressão. Tema genuinamente curto pode fechar em oito.

**No máximo um slide de contraste binário** por carrossel (do tipo "isso é defesa / aquilo é ataque"). É um beat forte, e dois ou mais viram fórmula — o olho treinado reconhece como texto de robô.

## O briefing de arte

Cada slide com arte recebe um briefing de uma linha: **o que desenhar e como compor**. Concreto, sempre. "Balde furado vazando moedas pelas laterais" se desenha; "ineficiência operacional" não.

A composição muda conforme a disposição, porque o corte é diferente:

- **Para `l-bottom`:** o assunto na **metade de baixo**, espaço vazio no topo. O texto vai ocupar a parte de cima.
- **Para `l-right` e `l-left`:** assunto **centralizado e robusto**, porque a arte vai ser cortada na vertical e só metade aparece.
- **Para `cover`:** cena cheia, com **área escura ou vazia no topo** para o título pousar.

Exporta em PNG, na resolução do slide (1080 de largura basta; 2160 se quiser folga), e salva em `arte/` com o nome do slide.

## O pipeline técnico

- **Montagem:** `templates/modelo.html`, trocando conteúdo, arte e variáveis de cor.
- **Render e corte:** `python scripts/render_slice.py carrossel.html slides/ 10` — abre o Chrome em modo invisível, tira uma captura da pilha inteira e fatia em imagens de 1080×1350.
- **No Windows**, rode com `PYTHONUTF8=1` na frente do comando para evitar erro de acento.
- Depois de renderizar, **abre os PNGs e olha**. Capa e slides de meia-página são os que mais quebram.
