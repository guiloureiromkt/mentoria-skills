# A ficha do harness (10 campos)

Preencha antes de mexer em qualquer arquivo. Ela é o `intent` do harness: se você tem o cycle instalado, ela vira `intent/<nome>.md` quase sem edição. A skill `mentoria:harness` faz as perguntas por você.

| Campo | A pergunta | Exemplo (mídia paga) |
|---|---|---|
| **1. Propósito** | O que este harness faz, para quem, e o que nunca faz? | Opera a mídia paga da Garimp.ai. Não produz criativo. |
| **2. Método** | Onde entra o ciclo e onde entra o graph? Que portões este harness pede (dinheiro · permissão · dado destrutivo · superfície de usuário)? | Cycle aqui dentro. Portão de dinheiro: verificador separado. Graph a cada 4 semanas. |
| **3. Peças** | O que vira template, skill, loop e agente? (template: custa zero · skill: rodou 3× na mão sem mudar · loop: skill que rodou 3× sem correção · agente: precisa não ver o resto, ou confere outro) | Agentes: analista, executor, verificador. Loops: diário e semanal. |
| **4. Comprar ou construir** | O que já existe pronto e passa nos 4 gates (serve · licença comercial · não inunda · não roda código obscuro)? O que é seu e ninguém tem? | Instala MCP do Google Ads e do Meta. Constrói nomenclatura e relatório na sua língua. |
| **5. Fontes** | De onde bebe: arquivo no repositório, plataforma por API, outro harness (só a pasta `saida/` dele)? | Ads por MCP, verba em arquivo, criativos de `../garimpai-social/saida/`. |
| **6. APIs e conectores** | Quais são necessários e quais têm caminho grátis? | Todos grátis. Meta: liberar só a conta certa. |
| **7. Interface** | Como a pessoa usa: chat na pasta · pasta de aprovação · portal com MCP? | Chat + `aprovar/`. Sem portal. |
| **8. Hospedagem** | Onde mora: repositório, Actions, máquina, VPS, Drive? | Repositório privado + Actions. |
| **9. Acesso e permissão** | Quem entra, o que pode, o que é bloqueado (três camadas)? | Só o Eduardo. |
| **10. Custo e operação** | De quem é o token em cada uso? Qual a rotina, o que é automático, o que espera aprovação? | Actions com chave da empresa e teto. Nada sobe sem `aprovado/`. |

## A lista "fica fora, e onde mora"

Toda função que a pessoa quer e não entra neste harness ganha uma linha aqui. É o antídoto contra o sumiço: o módulo inteiro que cai do roadmap sem ninguém decidir.

| Função | Por que não entra aqui | Onde mora (outro harness · arsenal · fica mapeado) |
|---|---|---|
| | | |

## Exemplo preenchido: harness de conciliação (financeiro)

| Campo | Resposta |
|---|---|
| Propósito | Fechar o período de conciliação mensal da empresa: pagamentos, frete, provedor de pagamento e notas. Não paga nada: prepara, confere e pede aprovação. |
| Método | Cycle aqui dentro. Portões: dinheiro e dado sigiloso (folha, fornecedores) → verificador separado em toda ação. |
| Peças | Templates: checklist datado do mês. Skills: baixar-boletos, baixar-notas, cruzar-extrato. Loops: loop-do-dia (lê o checklist, faz o passo do dia, para em qualquer passo que pague). Agentes: auditor (mensal, só lê, direciona achados), verificador. |
| Comprar ou construir | Instala: MCP do Gmail (lê, rotula, baixa anexo; não envia), rclone para o Drive. Constrói: o checklist, o cruzamento, o achados/. |
| Fontes | E-mail de nota fiscal (plataforma), boletos do frete (plataforma), extrato do provedor (export), planilha de folha (arquivo no repositório, sigilosa). |
| APIs e conectores | Gmail grátis; Drive grátis; provedor de pagamento: export manual até ter API. |
| Interface | Chat + `aprovar/`. Carol aprova pagamento no arquivo. |
| Hospedagem | Repositório privado + cron na máquina (precisa do Drive local); Actions só para o que não precisa da máquina. |
| Acesso e permissão | Paulo: tudo. Carol: `aprovar/` e `saida/`. Ninguém mais. Sem acesso ao repositório de marketing. |
| Custo e operação | Loops com chave da empresa e teto. Diário: passo do checklist. Mensal: auditoria. Pagamento nunca é automático. |
