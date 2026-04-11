# 📝 Fase 1 – Especificação: Jogo da Memória

### 👥 Grupo `PM.08.2024151531`
*   👨‍💻 **Rafael Junqueira (Leader)** — 2024151531
*   👨‍💻 **Diogo Brito** — 2024151350

**Docente de Labratório:** Patrícia Macedo
**Aula PL:** PL8

### 🕹️ 1. Descrição do Jogo
O objetivo do jogo é encontrar todos os pares de símbolos escondidos numa grelha. O diferencial desta versão é a introdução de elementos estratégicos através de cartas com comportamentos dinâmicos.

*   **🔤 Símbolos:** As cartas utilizam identificadores simples (ex: "A", "B", "C").
    *   **Consola:** Representação textual simples.
    *   **JavaFX:** Representação visual através de **Emojis** (ex: 🍎, 🍌, 🍒).
*   **🃏 Cartas Especiais:** 
    *   `[!]` **Bónus:** Ao ser revelada, oferece mais 3 tentativas ao jogador.
    *   `[?]` **Baralhar:** Ao ser revelada, baralha todas as cartas que ainda estão escondidas no tabuleiro.
*   **🏆 Condições de Vitória/Derrota:**
    *   **Vitória:** Encontrar todos os pares existentes.
    *   **Derrota:** O contador de tentativas chegar a zero (limite inicial de 15 jogadas).

---

### 🧠 2. Modelação do Domínio

A lógica do sistema foi desenhada para garantir a total separação entre o "cérebro" do jogo e a forma como ele é apresentado ao utilizador (Consola ou JavaFX).

#### 2.1. Identificação de Entidades e Responsabilidades

| | Entidade | Responsabilidade Principal |
| :--- | :--- | :--- |
| 🎮 | **MotorJogo** | **Controlador:** Gere as regras de negócio, controla o fluxo de turnos, valida pares, atualiza o contador de tentativas e verifica o estado de vitória/derrota. |
| 🗺️ | **Tabuleiro** | **Agregador:** Responsável pela criação da grelha, pelo baralhamento das cartas e por fornecer ao motor de jogo o acesso às peças em posições específicas. |
| 🃏 | **Carta (Abstrata)** | **Conceito Base:** Define a estrutura comum (símbolo e estado de visibilidade). Não pode ser instanciada, servindo de molde para as cartas reais. |
| 🃏 | **CartaNormal** | **Peça Padrão:** Representa uma carta comum cujo único objetivo é formar pares com outra carta idêntica. |
| ✨ | **CartaEspecial** | **Peça de Ação:** Contém o método `aplicarEfeito()` que altera variáveis globais do jogo (como as tentativas) no momento em que é revelada. |

#### 2.2. Relações Estruturais (POO)

*   **🔼 Herança:** As classes `CartaNormal` e `CartaEspecial` são especializações da classe `Carta`. Isto permite que o tabuleiro e o motor tratem todas as peças de forma genérica.
*   **💎 Composição:** O `Tabuleiro` **contém** uma lista de objetos `Carta`. O tabuleiro é o responsável por criar e gerir a existência destas cartas.
*   **🔌 Associação:** O `MotorJogo` **usa** o `Tabuleiro` para consultar o estado das cartas. Existe uma ligação onde o motor delega ao tabuleiro a gestão das posições.

---

### 📊 3. Modelo de Classes (UML)

O diagrama seguinte representa a arquitetura técnica do sistema:

![Diagrama UML](uml_parcial.png)

*   **Hierarquia:** Organização clara entre a classe abstrata e as suas subclasses.
*   **Encapsulamento:** Todos os atributos (como o símbolo ou as tentativas) são protegidos por modificadores de acesso privados.
*   **Polimorfismo:** O método `revelar()` é redefinido (@Override) na `CartaEspecial` para que o efeito de bónus seja ativado automaticamente via despacho dinâmico.

---

### 🖥️ 4. Protótipo da Interface Gráfica
A interação é feita através de coordenadas numéricas.

```text
Tentativas: 12 | Pares: 1/8
   0  1  2  3
0 [?] [*] [*] [!]
1 [*] [A] [A] [*]
Escolha a linha e coluna (ex: 0 1): 
```
*   `[*]` Carta virada para baixo.
*   `[A/B/C]` Carta normal revelada.
*   `[! / ?]` Carta especial revelada.
