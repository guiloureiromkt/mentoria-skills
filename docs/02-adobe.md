# Ligar o Illustrator no Claude

Aviso antes de começar: **esta não é uma tarefa pra fazer sozinha.** Diferente do Canva, que são dois minutos, aqui tem instalação de verdade — terminal, plugin, modo desenvolvedor. É assunto de aula com tela compartilhada. Este documento existe para você saber o que vem pela frente e o que já dá pra ir deixando pronto.

## Existem duas coisas com nome parecido, e confundir custa caro

**(a) O conector oficial "Adobe for Creativity"** — instala pelo painel de conectores do Claude, sem terminal, igual ao Canva. O problema: ele opera no nível do **Adobe Express**, não do Illustrator. Para o teu trabalho, que é vetor no Illustrator, serve pouco.

**(b) O `adb-mcp`** — um servidor feito por Mike Chambers que alcança Photoshop, **Illustrator**, InDesign, After Effects e Premiere. É esse que serve pra você.

Servidor aqui não é nada assustador: é um programinha que fica rodando na tua máquina e serve de tradutor entre o Claude e o Illustrator.

## O que precisa existir na máquina

- Python 3
- Node.js
- Adobe UXP Developer Tool (baixa pelo Creative Cloud)
- Claude Desktop (o aplicativo, não o navegador)
- O app da Adobe que você vai controlar

## O caminho, em resumo

1. Clonar o repositório `github.com/mikechambers/adb-mcp`
2. Instalar o MCP do aplicativo desejado
3. Subir o proxy (`node proxy.js`, ou o executável pronto que vem nas releases)
4. Instalar o plugin. **Aqui está a parte chata:** Photoshop, Premiere e InDesign usam UXP, que é simples. **Illustrator e After Effects usam CEP**, que pede criar um atalho especial (symlink) dentro da pasta de extensões da Adobe. É onde a instalação costuma travar.
5. Ativar o **Modo Desenvolvedor** em Configurações → Plugins, dentro de cada app da Adobe
6. No Claude Desktop: botão "+" → "Add from Adobe" → `config://get_instructions`

## O que esperar — e o que não esperar

A própria documentação do projeto avisa de três limitações, e vale saber antes para não se frustrar:

- **A IA erra posicionamento e tamanho de texto.** Isso bate direto na tua queixa de que "os textos ficam tudo borrados" no GPT. Aqui o problema é outro (não é resolução, é medida), mas o sintoma incomoda igual.
- **A lista de fontes é cortada nas primeiras mil, em ordem alfabética.** Se a fonte da marca começa com S, pode não aparecer.
- **O plugin precisa ser recarregado toda vez que o app reinicia.** Não é uma vez e pronto; é parte da rotina.

## A ordem que eu recomendo

1. **Canva agora**, sozinha, em dois minutos. É a primeira vitória com integração e não tem risco.
2. **Illustrator na aula**, com tela compartilhada, quando o assunto for o fluxo de artes.
3. **Template e brandbook replicável** só depois que o Illustrator estiver de pé — antes disso, é construir no vazio.

---
*Fonte: github.com/mikechambers/adb-mcp e a documentação do projeto. Levantado em 28/08/2026, revisado em 12/09/2026. Ainda não instalado por nós — quando instalarmos juntos, este documento vira o passo a passo real, com os tropeços anotados.*
