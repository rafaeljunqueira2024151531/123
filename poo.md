# Jogo da Memoria

Projeto desenvolvido no ambito da unidade curricular de Programacao Orientada a Objetos.

## Grupo

- Rafael Junqueira - 2024151531
- Diogo Brito - 2024151350

Grupo: PM.08.2024151531

## Descricao

Este projeto implementa um jogo da memoria em Java com interface grafica JavaFX.

O objetivo do jogo e encontrar todos os pares de cartas antes de acabarem as tentativas. O jogo inclui cartas normais, representadas por imagens, e cartas especiais que alteram o estado da partida.

## Regras do Jogo

- O jogador escolhe uma dificuldade no ecra inicial.
- Em cada jogada, o jogador revela duas cartas normais.
- Se as cartas forem iguais, o par e encontrado e as cartas desaparecem do tabuleiro.
- Se as cartas forem diferentes, voltam a ficar viradas para baixo.
- O jogador perde uma tentativa por cada par de cartas normais escolhido.
- O jogo termina quando todos os pares sao encontrados ou quando as tentativas chegam a zero.

## Dificuldades

- Facil: tabuleiro 4x4, 2 cartas especiais, 12 tentativas.
- Medio: tabuleiro 6x6, 4 cartas especiais, 28 tentativas.
- Dificil: tabuleiro 8x8, 6 cartas especiais, 44 tentativas.

## Cartas Especiais

- `!` Bonus: adiciona tentativas ao jogador.
- `?` Baralhar: baralha as cartas que ainda nao foram fixadas.

As cartas especiais sao ativadas com apenas um clique.

## Conceitos de POO Utilizados

- Encapsulamento: atributos privados e acesso por metodos publicos.
- Heranca: `NormalCard` e `SpecialCard` herdam de `Card`.
- Polimorfismo: cada tipo de carta redefine o metodo `reveal`.
- Excecoes: `InvalidBoardException` e `InvalidMoveException`.
- Separacao de responsabilidades:
  - `model`: logica do jogo.
  - `ui`: interface grafica.
  - `controller`: ligacao entre interface e modelo.

## Estrutura do Projeto

```text
src/main/java
├── Main.java
├── controller
│   ├── GameController.java
│   └── StartController.java
├── exception
│   ├── InvalidBoardException.java
│   └── InvalidMoveException.java
├── model
│   ├── Board.java
│   ├── Card.java
│   ├── GameDifficulty.java
│   ├── GameEngine.java
│   ├── NormalCard.java
│   └── SpecialCard.java
└── ui
    ├── GameView.java
    └── StartView.java
```

As imagens das cartas estao em:

```text
src/main/resources/images
```

## Requisitos

- Java 17
- Maven
- JavaFX

## Como Executar

Na raiz do projeto, executar:

```bash
mvn javafx:run
```

Tambem e possivel executar pelo IntelliJ IDEA, correndo a classe `Main`.

## Como Jogar

1. Abrir a aplicacao.
2. Escolher a dificuldade.
3. Clicar em `Iniciar jogo`.
4. Escolher cartas no tabuleiro.
5. Encontrar todos os pares antes das tentativas acabarem.

## Testes

Os testes unitarios devem incidir sobre o modelo do dominio, principalmente:

- criacao valida e invalida do tabuleiro;
- validacao de jogadas;
- funcionamento das cartas especiais;
- condicoes de vitoria e derrota.

Para executar os testes:

```bash
mvn test
```

## Observacoes

A interface grafica foi feita com JavaFX. A logica do jogo esta separada da interface, permitindo testar o modelo sem depender da parte grafica.
