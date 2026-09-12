# Ligar o Canva no Claude

O Canva tem conector oficial dentro do Claude. Conector é uma ponte pronta: você autoriza uma vez, e o Claude passa a conseguir criar, preencher e exportar design na tua conta do Canva sem você sair da conversa. Não precisa instalar nada.

**Onde isso funciona:** no Claude do navegador (claude.ai) e no aplicativo de computador. **Não** funciona dentro do Claude Code, que é o do terminal — lá o trabalho é com arquivo, não com conector.

## O passo a passo

1. Abre o **claude.ai** e entra na tua conta.
2. Clica no **teu nome, no canto inferior esquerdo** → **Configurações** (Settings).
3. Vai em **Conectores** (Connectors).
4. Procura **Canva** na lista. Se não estiver ali, clica em **Procurar conectores** (Browse connectors) e busca por "Canva".
5. Clica em conectar. Vai abrir a tela do Canva pedindo login e pedindo permissão. Confere o que está sendo autorizado e aceita.
6. Volta pro Claude, abre uma **conversa nova** e clica no ícone de ferramentas/configurações da conversa para confirmar que o Canva está ligado ali.

Pronto. A partir daí você pede em português: "cria no Canva um post 1080x1350 com esse texto", "preenche esse template com esses dados", "exporta esse design em PDF".

## O que dá pra fazer com ele ligado

Criar design novo pelo Canva AI, preencher template automaticamente (autofill), achar design que já existe na tua conta, e exportar em PDF ou imagem.

## Sobre planos — e uma correção

Na nossa primeira aula eu te disse que a integração **só** funcionava com o Canva Pro. Pela documentação atual, **não é bem assim**: o conector funciona com conta gratuita do Canva.

O que exige o **Pro** é outra coisa: o acervo de elementos premium e os recursos de Brand Kit. Como o teu motivo para querer o Canva é exatamente o acervo ("tem coisa que eu não acharia pra baixar"), a conclusão prática continua a mesma — mas a razão é outra, e você merece a razão certa.

Do lado do Claude, os conectores rodam nos planos pagos. No plano grátis existe restrição.

## Se der errado

**O Canva não aparece na lista de conectores.** Confere se você está no claude.ai e não no Claude Code, e se tua conta é paga.

**Autorizei e o Claude diz que não tem acesso.** Abre uma conversa nova — conversa antiga não enxerga conector ligado depois.

**Conectei a conta errada do Canva.** Volta em Conectores, desconecta, e conecta de novo com a conta certa.

---
*Fonte: central de ajuda do Canva sobre conectar assistentes de IA (canva.com/help/mcp-agent-setup) e a tela de conectores do próprio Claude. Conferido em 12/09/2026.*
