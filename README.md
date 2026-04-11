### Fase 1 – Especificação: Jogo da Memória "POO-Match"

#### 1. Descrição do Jogo
*   **Objetivo:** Encontrar todos os pares de símbolos numa grelha.
*   **Simbolos:** Usaremos **Strings** simples para os símbolos (ex: "A", "B", "C"). 
    *   Na **Consola**, imprimimos o texto.
    *   No **JavaFX**, os símbolos das cartas serão representados por Emojis (🍎, 🍌).
*   **Cartas Especiais:** 
    *   `[!]` (Bónus): Quando virada, dá mais 3 tentativas ao jogador.
    *   `[?]` (Baralhar): Quando virada, baralha as cartas que ainda estão escondidas.
*   **Condições de vitória/derrota:**
    *   **Vitória:** Todos os pares encontrados.
    *   **Derrota:** Acabarem as tentativas (ex: limite de 15 jogadas).

#### 2. Modelação do Domínio

*   **Entidades Principais:**
    1.  **Carta (Abstrata):** Guarda o símbolo (`String`) e o estado (`escondida`, `fixa`).
    2.  **CartaNormal:** Comportamento padrão de par.
    3.  **CartaEspecial:** Tem um método `aplicarEfeito()` que muda o estado do jogo.
    4.  **Tabuleiro:** Uma lista de `Carta`. Sabe baralhar e validar se duas cartas são iguais.
    5.  **MotorJogo:** Gere a pontuação, o número de tentativas e o estado atual (venceu/perdeu).

#### 3. Modelo de Classes (UML)
![Diagrama UML](uml_parcial.png)

*   **Herarquia de Herança:**
    *   `abstract class Carta`
        *   `class CartaNormal extends Carta`
        *   `class CartaEspecial extends Carta`
*   **Composição:**
    *   `Tabuleiro` **contém** uma `List<Carta>`.
*   **Polimorfismo:**
    *   O método `revelar()` existe na classe `Carta`. Na `CartaEspecial`, ele faz @Override para também ativar o efeito especial.

#### 4. Protótipo da Interface Gráfica

```text
Tentativas: 12 | Pares: 1/8
   0  1  2  3
0 [?] [*] [*] [!]
1 [*] [A] [A] [*]
Escolha a linha e coluna (ex: 0 1): 
```
*   `[*]` representa carta virada para baixo.
*   Letras representam cartas normais.
*   `[!/?]` representaria a especial.

---
