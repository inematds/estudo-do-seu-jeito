# estudo-do-seu-jeito

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

**Você vai conseguir ensinar o seu filho (ou o seu aluno) do jeito que ele aprende, mesmo sem dominar a matéria.**
Este kit é um ajudante de quem ensina. Ele organiza o guia de estudo por objetivo, confere cada questão na fonte
e mostra, às claras, qual método de estudo está funcionando.

📖 Guia (landing + passo a passo): **https://inematds.github.io/estudo-do-seu-jeito/guia/**

## A história que deu origem à fórmula

Lúcia é mãe de quatro filhos e tem há 21 anos uma agência de marketing com o marido, dentro de casa. A filha mais
velha, Clara, foi estudar biologia marinha numa faculdade a cinco horas de casa. Clara, que só tirava nota máxima,
começou a ir mal numa matéria de que gostava: muito conteúdo em pouco tempo, aulas com slides cheios de texto e a
regra do professor de que **errar uma questão de um objetivo de aprendizagem faz perder o objetivo inteiro**.

Clara não gostava de IA. Lúcia não é programadora. Mesmo assim, Lúcia estudou duas a três horas por dia com o Claude
para conseguir ensinar a filha e depois montou um guia de estudo do jeito de Clara, que é visual: esquemas para
redesenhar, exemplos da vida real, pegadinhas, questões e folhas de resumo para imprimir. A primeira versão saiu num
dia, com um pedido de quatro frases no chat; depois Lúcia passou para o Claude Code para ter partes interativas.
Toda semana Clara mandava fotos das anotações, e o guia era refeito e conferido no livro. A nota subiu mais de 10
pontos, de um D alto para perto de 80. Os objetivos que Clara tinha perdido na prova 2 voltaram todos certos na
prova 3.

(Personagens com nomes trocados. Os números acima são da história; **não foram medidos por este kit**. O exemplo que vem
no kit usa dados inventados.)

## A fórmula em 8 passos

| # | Passo | No kit |
|---|---|---|
| 1 | **Quem ensina aprende primeiro**: estude o ponto em que o aluno errou, com a IA explicando a partir da fonte | `estudo tutor`, prompt 4 |
| 2 | **Entender como o professor avalia**: o que faz perder ponto | `professor` no materia.json |
| 3 | **Entender como o aluno aprende**: visual, falado, vida real, escrita | `aluno.jeito` |
| 4 | **Partir do que ele já errou** | `estudo resultado --origem prova` |
| 5 | **Planejar antes de construir**: a IA pergunta o que não sabe, dá opções e fecha num resumo | prompts 1 e 2 → `plano.md` |
| 6 | **Guia por objetivo, só com o que está na fonte**: leitura, visual, vida real, pegadinhas, questões | `estudo adicionar` (recusa questão sem prova), `estudo guia` |
| 7 | **Toda semana: material novo e conferência** | `estudo semana`, prompt 5, `estudo respostas` |
| 8 | **Passar o bastão**: o aluno passa a usar sozinho | guia.html → `estudo importar`, prompt 8 |

`python3 -m estudo passos` mostra o estado de cada passo, calculado dos seus dados.

## O teste dos métodos, às claras

Ninguém sabe de antemão qual método funciona para cada aluno. O kit testa e mostra tudo:

1. Antes de estudar um objetivo, o método é escolhido e **anotado no diário com o motivo** (`estudo proximo --anotar`).
   O kit alterna entre os métodos que combinam com o jeito do aluno e um controle (reler e grifar), para o teste ser justo.
2. O resultado conta para o método anotado por último naquele objetivo.
3. "Dominado" segue a regra do professor (acertar todas, se for assim que ele corrige).
4. Com menos de 3 objetivos, o método aparece como **"pouco dado"** e nunca como o melhor. Para dizer que um está na frente,
   são precisos dois métodos com dados e 20 pontos de diferença.
5. O diário (`diario.jsonl`) só recebe linhas novas, nunca apaga; `estudo diario` mostra tudo.

Métodos: ver e redesenhar · explicar em voz alta · exemplo da vida real · questões sem consultar · reler e grifar (controle).

## Quem escreve e quem confere

**O kit não lê foto nem escreve conteúdo.** Quem transcreve as anotações e escreve objetivos e questões é você ou a IA
(chat, Claude Code, Codex ou o cérebro do seu Jarvis). O kit **organiza, confere e registra**:

- cada questão diz de qual fonte saiu e copia o trecho; o kit procura esse trecho no texto da fonte e **recusa** a questão
  se ele não existir (sem diferença de acento ou maiúscula);
- resposta preenchida pelo aluno que não bate com a fonte é apontada antes de virar material de estudo;
- a IA não cria questão extra "de cabeça": quando falta questão, falta fonte.

## Quatro jeitos de usar

| Jeito | Para quem | Como |
|---|---|---|
| **Chat** (qualquer IA) | quem não quer instalar nada | `python3 -m estudo prompts` (8 prompts, PT/EN/ES) ou copie de `estudo/prompts/` |
| **App visual** | o aluno | `guia.html`: abre no celular ou no computador, sem internet |
| **Claude Code / Codex** | quem ensina e quer o agente fazendo o trabalho | skill em `skill/estudo-do-seu-jeito/` |
| **Jarvis (INTELECTO v2)** | quem já tem o assistente | plugin `estudo`: 6 ferramentas |

## Em 1 minuto

Precisa de Python 3.10 ou mais novo. Nenhum pacote para instalar.

```bash
git clone https://github.com/inematds/estudo-do-seu-jeito && cd estudo-do-seu-jeito
python3 -m estudo demo --pasta ~/estudo-demo     # exemplo com dados inventados
# abra ~/estudo-demo/guia.html no navegador
python3 -m estudo placar --pasta ~/estudo-demo
```

Para a sua matéria (os dados ficam em `~/.estudo-do-seu-jeito`, fora do repositório):

```bash
python3 -m estudo nova "Biologia"
python3 -m estudo prompts 1                       # planejar no chat
python3 -m estudo semana anotacoes-aula-5.txt     # fonte da semana
python3 -m estudo adicionar objetivos.json        # recusa questão sem prova na fonte
python3 -m estudo proximo --anotar                # método de cada objetivo, com o porquê
python3 -m estudo guia                            # ~/.estudo-do-seu-jeito/guia.html
python3 -m estudo importar resultados.json        # o que o aluno fez no app
python3 -m estudo plano-prova --data 2026-12-05
```

Qualquer comando aceita `--json` (para agentes) e `--pasta` (uma pasta por matéria).

## Skill no Claude Code

```bash
mkdir -p ~/.claude/skills && cp -r skill/estudo-do-seu-jeito ~/.claude/skills/
```

Depois, dentro da pasta do kit: "use a skill estudo-do-seu-jeito e me ajude a montar o guia da minha filha".
Sem a skill, funciona colando o prompt 3 (`python3 -m estudo prompts 3`). No Codex: peça para ler o
`skill/estudo-do-seu-jeito/SKILL.md` e seguir.

## Plugin do INTELECTO v2 (seu Jarvis)

```bash
pip install git+https://github.com/inematds/estudo-do-seu-jeito
INTELECTO_PLUGINS=estudo ESTUDO_PASTA=~/.estudo-do-seu-jeito python3 -m intelecto
```

Ferramentas: `estudo_passos`, `estudo_placar`, `estudo_proximo_metodo`, `estudo_registrar_resultado`,
`estudo_conferir`, `estudo_plano_prova`. Nenhuma roda comando nem lê fora da pasta da matéria; as que gravam só
acrescentam linhas no diário. Pelo Telegram do Jarvis, o aluno pode mandar "fiz 3 de 3 em respiração" e
perguntar "qual método está funcionando?".

## Como está montado

| Arquivo | O que faz |
|---|---|
| `estudo/dados.py` | pasta da matéria, materia.json, fontes, diário (só acrescenta) |
| `estudo/verificador.py` | confere trecho na fonte, opções, respostas do aluno |
| `estudo/experimento.py` | placar dos métodos, escolha do próximo com o motivo |
| `estudo/formula.py` | os 8 passos e o estado de cada um |
| `estudo/plano.py` | plano dia a dia até a prova |
| `estudo/guia_html.py` | o app do aluno (HTML único) |
| `estudo/ferramentas.py`, `intelecto_plugin.py` | ferramentas para agentes e o plugin do Jarvis |
| `estudo/prompts/{pt,en,es}/` | os 8 prompts para o chat |
| `estudo/exemplo/` | a matéria de exemplo (biologia, dados inventados) |

Testes: `python3 -m pytest -q testes`.

## Limites desta versão (v0.1)

- A interface (comandos e app) está em português; os prompts estão em PT, EN e ES.
- O kit não lê imagem: a transcrição das fotos é feita pela IA ou por você (prompt 5).
- A conferência acha o trecho na fonte, mas não garante que a fonte esteja certa nem que o trecho prove a resposta;
  quando nenhuma palavra da resposta aparece no trecho, ela avisa.
- O placar compara objetivos diferentes, que têm dificuldades diferentes: é uma pista honesta, não um experimento científico.
- Os resultados do app ficam no navegador até você exportar e importar.

## Licença

MIT.
