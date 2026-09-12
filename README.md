# Skills — Mentoria Mão na Massa

As ferramentas que a gente vai usar na mentoria. Cada pasta aqui dentro é uma **skill**: um conjunto de instruções que o Claude lê sozinho quando o assunto aparece. Você instala uma vez e esquece que existe — ela entra em cena quando faz sentido.

## Começa por aqui

**[docs/00-como-instalar.md](docs/00-como-instalar.md)** — instalação em um comando, e como conferir se deu certo.

Se quiser ir direto:

```bash
git clone https://github.com/SEU-USUARIO/skills-iza.git ~/skills-iza && bash ~/skills-iza/instalar.sh
```

No Windows, o comando de PowerShell está no documento de instalação.

## O que vem instalado

| Skill | O que faz | Como chamar |
|---|---|---|
| **carrossel** | Carrossel de Instagram de 8 a 10 slides a partir de um tema ou de um material do cliente. Estrutura a história, diagrama, monta o HTML e corta os slides em 1080×1350. **A arte é tua** — nada aqui gera imagem por IA | "monta um carrossel sobre X" |
| **trendseeker** | Varredura semanal do teu mercado: o que mudou de regra, que ferramenta apareceu, que dor nova o cliente está sentindo. Devolve sinais com fonte e data | "roda o trendseeker" |
| **impeccable** | Design de site e de página — cria, critica, audita, melhora. É a que te tira do visual genérico | "redesenha essa página" |
| **find-skills** | Acha e instala outras skills quando você precisa de uma que não tem | "acha uma skill pra editar vídeo" |

E em **[docs/03-mais-skills.md](docs/03-mais-skills.md)**: `deep-research` (pesquisa com fonte e bibliografia), `taste` (mais repertório visual) e o meu marketplace, que traz a skill de construir site inteiro.

## As integrações

- **[docs/01-canva.md](docs/01-canva.md)** — ligar o Canva no Claude. Dois minutos, você faz sozinha, sem instalar nada.
- **[docs/02-adobe.md](docs/02-adobe.md)** — ligar o Illustrator no Claude. **Não faz sozinha** — é aula com tela compartilhada. O documento serve pra você saber o que vem pela frente.

## Duas coisas antes de começar

**A `carrossel` precisa de um arquivo `marca.md`** na pasta do projeto, com as cores, as fontes e a voz daquela marca. Se não existir, a skill te entrevista e cria. É o mesmo princípio do teu arquivo mãe: escreveu uma vez, não reexplica mais.

**A `trendseeker` precisa de um `mercado.md`**, com quem você atende e o que te interessa acompanhar. Mesma coisa: ela pergunta e monta com você na primeira vez.

## Se travar

Tira print da tela inteira e me manda. É mais rápido eu ver o erro do que ler a descrição dele.

---

### Créditos e licenças

`carrossel` e `trendseeker` são minhas, sob licença MIT — pode usar, mudar e levar pra onde quiser.

`impeccable` é de terceiros, sob Apache 2.0, redistribuída aqui sem modificação, com a licença original dentro da pasta. `find-skills` vem do ecossistema aberto de Agent Skills, também sem modificação.
