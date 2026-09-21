---
name: fila-de-aprovacao
description: Separa toda ação para fora (subir campanha, pausar conjunto, publicar, enviar, pagar) em três momentos com arquivo. Propor escreve o pedido em aprovar/; uma pessoa aprova movendo para aprovado/; executar faz só o que está aprovado e chama um verificador em contexto separado para conferir. Use quando um loop ou agente precisar agir no mundo sem ninguém no teclado, quando pedir "propõe e espera aprovação", "executa o que foi aprovado", "o que tem na fila", ou dentro de qualquer harness clonado do harness-template. Nunca executa a partir de aprovar/, nunca depois do prazo, nunca confere o próprio trabalho.
---

# Fila de aprovação — propor, aprovar, executar, conferir

O problema que esta skill resolve tem dois lados ruins. Um loop que age sozinho no mundo (pausa campanha, publica, envia e-mail, paga boleto) não merece confiança. Um loop que para e espera alguém na frente do computador não roda de madrugada. A fila fica no meio: **o loop propõe por escrito, uma pessoa aprova por escrito, e só então a ação acontece, conferida por outro que não a fez.**

Tudo é arquivo. Não tem portal, não tem botão, não tem banco. Quem aprova pode fazer pelo GitHub no navegador, pelo Drive ou pelo Obsidian.

## As duas pastas

| Pasta | O que tem dentro | Quem escreve |
|---|---|---|
| `aprovar/` | pedidos de ação, um arquivo por ação, no formato de `references/formato.md` | o loop ou o agente que quer agir |
| `aprovado/` | os mesmos arquivos, depois que uma pessoa escreveu `aprovado_por` e moveu para cá; depois da execução, ganham `executado_por` e `verificado_por` | a pessoa (mover) · o executor e o verificador (acrescentar linhas) |

Se as pastas não existem, a skill cria as duas e o `aprovar/README.md` do template. Se o harness veio do `harness-template`, já estão lá.

## Os princípios que não se quebram

1. **Nada é executado a partir de `aprovar/`.** Só de `aprovado/`, e só com `aprovado_por` preenchido com nome e data.
2. **Prazo vencido não se executa.** Todo pedido tem `prazo`. Passou, o arquivo fica em `aprovar/` como registro e a skill diz "venceu", não age.
3. **Executa o que está escrito, nem mais nem menos.** A seção "O que vai ser feito, exatamente" é o contrato. Se na hora de executar a situação mudou (o conjunto já foi pausado, o post já saiu), a skill não improvisa: escreve o que encontrou e para.
4. **Quem confere não é quem fez.** A verificação roda em contexto separado, com o arquivo aprovado e a evidência, sem o histórico da execução. Se o plugin `cycle` está instalado, é o agente `cycle:verifier`; se não, um subagente novo com a instrução de `references/verificador.md`.
5. **Evidência ou não aconteceu.** Print, resposta da API, id do objeto criado, ou o arquivo de saída. Vai para `saida/evidencias/` e o caminho entra no arquivo aprovado.
6. **Dinheiro nunca é automático.** Pedido cuja ação é pagar, transferir ou reembolsar é proposto e aprovado como qualquer outro, mas a execução é sempre de uma pessoa: a skill prepara (boleto baixado, valor conferido, destinatário) e para.

## Os quatro modos

### `propor`
Quem chama: um loop ou agente que decidiu que uma ação para fora é necessária. A skill escreve `aprovar/AAAA-MM-DD-<verbo>-<objeto>.md` com o formato de `references/formato.md`. Antes de gravar, confere:
- o motivo cita a origem do número (arquivo, plataforma, data), não uma impressão;
- `reversivel` diz como desfazer, ou diz "não" com todas as letras;
- `prazo` existe e é depois de agora;
- não há outro pedido aberto para o mesmo alvo (se há, acrescenta ao existente em vez de duplicar).

Se o harness tem `.claude/settings.json` negando a ação (por exemplo, sem acesso à plataforma), a skill escreve o pedido mesmo assim e avisa que a execução vai precisar de alguém com acesso.

### `status`
Lista a fila sem gastar token: `python3 scripts/fila.py` na raiz do harness. Devolve pendentes (com dias até o prazo), vencidos, aprovados a executar, executados sem verificação, e concluídos. É o primeiro comando de todo loop diário e de toda conversa que começa com "o que tem na fila".

### `executar`
Para cada arquivo em `aprovado/` com `aprovado_por` e sem `executado_por`:
1. Lê a seção "O que vai ser feito, exatamente" e a "O que NÃO vai ser feito".
2. Confere que o alvo ainda existe e está no estado esperado. Se não, escreve o que encontrou em `## Execução` e para naquele arquivo.
3. Faz cada passo numerado, na ordem, pela ferramenta que o harness permite (MCP, API, script). Nada fora da lista.
4. Guarda a evidência em `saida/evidencias/<nome-do-arquivo>/` e acrescenta ao arquivo:
   ```
   executado_por: <agente ou pessoa> · <data hora> · evidência: saida/evidencias/<...>
   ```
5. Chama `conferir` para esse arquivo. Nunca pula.

Ação de dinheiro: passos 1 e 2, depois prepara o que dá (arquivo, valor, destinatário conferido) e para com a linha `preparado_por`, esperando uma pessoa executar.

### `conferir`
Roda em contexto separado, sempre. Recebe só: o arquivo aprovado inteiro e o caminho da evidência. Responde a três perguntas, por escrito, no arquivo:
- O que foi feito é exatamente o que estava em "O que vai ser feito"? (item por item)
- Algo da lista "O que NÃO vai ser feito" aconteceu?
- A evidência prova, ou só afirma?

Acrescenta `verificado_por: <agente> · <data hora> · <ok | divergência: ...>`. Divergência não desfaz nada sozinha: vira um pedido novo em `aprovar/` ("reverter X", com o motivo), para a pessoa decidir.

## Como um loop usa isto

Um loop diário de mídia, por exemplo, faz nesta ordem: `status` → lê os dados do dia → se algo pede ação, `propor` → `executar` o que já estava aprovado de ontem → `conferir` → escreve o relatório em `saida/`. Ele nunca fica esperando: o que não está aprovado fica na fila até amanhã, e o que venceu fica como registro.

## O que esta skill não faz

- Não decide se uma ação é boa. Isso é do agente que propõe e da pessoa que aprova.
- Não aprova. Nem quando a pessoa diz "pode aprovar por mim". A aprovação é mover o arquivo com nome e data, feito por quem assina.
- Não manda mensagem, não publica, não paga por conta própria fora do que está em `aprovado/`.
- Não substitui o portão de produção do cycle: um deploy continua precisando de `.cycle/release-approval`.
