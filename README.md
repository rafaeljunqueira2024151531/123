# 🏢 Simulador de Elevadores em Prédio Virtual
### Programação Avançada 2025/26 — Fase 2 (Projeto Funcional)

---

## 📘 1. Descrição do Projeto
Este projeto implementa um simulador de elevadores funcional, que representa o funcionamento interno de um edifício com pisos, elevadores e passageiros.

A **Fase 2** expande o modelo base, introduzindo a lógica de simulação em tempo real, gestão de estados e interfaces de visualização.
As principais funcionalidades desta fase incluem:

- **Dois modos de visualização:** Interface Gráfica (JavaFX) e Modo Consola;
- **Motor de Simulação:** Controlo temporal e movimentação dos elevadores;
- **Padrões de Desenho:** Implementação de *Strategy* (algoritmos de decisão), *State* (estados do elevador) e *Factory* (criação de passageiros);
- **Configuração dinâmica:** Definição de nº de pisos, elevadores e tempos de simulação;
- **Estatísticas:** Monitorização de tempos de espera e passageiros transportados.

---

## 🧩 2. Estrutura do Projeto

```
src/
 ├── main/
 │   └── java/
 │       └── pt/ests/pa/
 │            ├── adt/               → Estruturas de dados genéricas
 │            ├── buildings/         → Lógica do Edifício
 │            ├── elevators/         → Elevadores e gestão de carga
 │            ├── floors/            → Pisos e filas de espera
 │            ├── gui/               → Interface JavaFX (Views e Controllers)
 │            ├── passengers/        → Passageiros e Fábricas
 │            ├── simulation/        → Motor de simulação
 │            ├── state/             → Padrão State (Idle, Moving, DoorsOpen)
 │            ├── strategy/          → Padrão Strategy (Algoritmos de elevador)
 │            ├── MainConsole.java   → Ponto de entrada (Modo Consola)
 │            └── MainJavaFX.java    → Ponto de entrada (Modo Gráfico)
 │
 └── test/
     └── java/
         └── pt/ests/pa/
            ├── adt/ArrayPriorityQueueTest
            ├── buildings/BuildingTest
            ├── elevators/ElevatorTest
            ├── floors/FloorTest
            ├── passengers/
            │   ├── PassengerTest
            │   ├── PassengerFactoryTest
            │   └── PassengerGeneratorTest
            ├── state/ (testes dos estados)
            ├── strategy/ (testes das estratégias)
            └── simulation/SimulationTest
```

---

## 🧱 3. Diagrama UML de Classes

O modelo segue uma arquitetura modular, organizada por pacotes, separando a lógica de negócio (Model) da visualização (View).

![Diagrama UML](uml_diagrama.png)

> **Resumo das Relações:**
> - `Simulation` controla o fluxo de tempo e interage com `Building`;
> - `Elevator` altera o seu comportamento consoante o seu `ElevatorState`;
> - As estratégias de movimento (`Strategy`) decidem qual elevador atende um pedido;
> - A `GUI` e a `Console` observam o estado do `Building` para renderizar a informação.

---

## ⚙️ 4. Execução e Testes

### 🧩 Requisitos:
- **JDK 17 ou superior**
- **Maven** (para build e dependências)
- **Bibliotecas JavaFX** (geridas pelo Maven)

### ▶️ Compilar o projeto:
```bash
mvn clean compile
```

### 🧪 Executar os testes unitários:
```bash
mvn test
```

### 🚀 4.1. Executar no **Modo Consola**

O modo consola corre a simulação passo a passo.

**Compilar:**

```bash
mvn clean compile
```

**Executar:**

```bash
mvn exec:java -Dexec.mainClass="pt.ests.pa.MainConsole"
```

**Exemplo de execução:**
Input pedido ao utilizador:

```yaml
Número de pisos: 8
Número de elevadores: 3
Capacidade dos elevadores: 5
Probabilidade de gerar passageiro (0-1): 0.25
```

**Comandos disponíveis:**

```text
ENTER  → avançar 1 step
p      → avançar 10 steps
q      → sair
```

### 🎨 4.2. Executar no Modo Gráfico (JavaFX)

**Compilar com JavaFX:**

```bash
mvn clean install
```

**Executar UI:**

```bash
mvn exec:java -Dexec.mainClass="pt.ests.pa.MainJavaFX"
```

---

## 📅 5. Estado da Fase 2

| Tarefa | Descrição | Estado |
|--------|------------|---------|
| Simulação | Motor de tempo e lógica de movimento | ✅ Concluído |
| Padrões | Implementação de State, Strategy e Factory | ✅ Concluído |
| Visualização | Modo Consola funcional | ✅ Concluído |
| Visualização | Modo JavaFX funcional | ✅ Concluído |
| Testes | Validação de cenários de simulação | ✅ Concluído |
| Documentação | Instruções de execução atualizadas | ✅ Concluído |

---

## 🎨 6. Interface Gráfica (Mockups e Implementação)

As imagens abaixo representam a disposição visual implementada na interface JavaFX, permitindo acompanhar o movimento dos elevadores e o estado das filas.

![Mockup da Interface](mockup1.png)
![Mockup da Interface](mockup2.png)
![Mockup da Interface](mockup3.png)

> A interface permite configurar os parâmetros iniciais e visualizar estatísticas em tempo real durante a execução da simulação.

---

## 👨‍💻 Autores

**Nomes:** Diogo Brito, Diogo Gomes e Rafael Junqueira  
**Unidade Curricular:** Programação Avançada (ESTS — 2025/26)  

**Fase:** 2 — Projeto Funcional
