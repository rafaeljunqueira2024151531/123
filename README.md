# 🏢 Simulador de Elevadores em Prédio Virtual
### Programação Avançada 2025/26 — Fase 3 (Entrega Final)

---

## 📘 1. Descrição do Projeto
Este projeto implementa um simulador de elevadores funcional, que representa o funcionamento interno de um edifício com pisos, elevadores e passageiros.

A **Fase 3 (Entrega Final)** foca-se na consolidação do projeto através da otimização da arquitetura via **Refactoring**, garantindo que o código cumpre os padrões de qualidade e os princípios da programação orientada a objetos lecionados.

As principais funcionalidades incluem:
- **Dois modos de visualização:** Interface Gráfica (JavaFX) e Modo Consola;
- **Motor de Simulação:** Controlo temporal e movimentação dos elevadores;
- **Padrões de Desenho:** Implementação de *Strategy* (algoritmos de decisão), *State* (estados do elevador) e *Factory* (criação de passageiros);
- **Configuração dinâmica:** Definição de nº de pisos, elevadores e tempos de simulação;
- **Estatísticas:** Monitorização de tempos de espera e passageiros transportados;
- **Refactoring & Clean Code (Novo):** Aplicação de técnicas para eliminação de *Code Smells* (Long Method, Magic Numbers e Message Chains).

---

## 🛠️ 2. Relatório de Refactorings (Fase 3)
De modo a melhorar a estrutura interna do programa sem alterar o seu comportamento, foram aplicadas as seguintes técnicas de refactoring:

| Técnica | Localização | Problema Resolvido (Smell) | Descrição |
|:--- |:--- |:--- |:--- |
| **Extract Method** | `Simulation.step()` | **Long Method** | O método `step()` era demasiado extenso. Foi decomposto nos métodos privados `generatePassengers()`, `processCalls()` e `updateElevators()` para melhorar a legibilidade e manutenção. |
| **Replace Magic Number** | `InitialConfigController` | **Magic Number** | O valor fixo `0.25` da probabilidade foi substituído pela constante simbólica `DEFAULT_PASSENGER_PROBABILITY`, facilitando a configuração global do sistema. |
| **Hide Delegate** | `Simulation` / `Controller` | **Message Chain** | Evitou-se a cadeia de mensagens `sim.getBuilding().getFloor(i).getWaitingCount()`. Criou-se o método `getFloorWaitingCount(i)` na `Simulation` para encapsular o acesso aos dados do edifício. |

---

## 🧩 3. Estrutura do Projeto

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

## 🧱 4. Diagrama UML de Classes

O modelo segue uma arquitetura modular, organizada por pacotes, separando a lógica de negócio (Model) da visualização (View).

![Diagrama UML](uml_diagrama.png)

> **Resumo das Relações:**
> - `Simulation` controla o fluxo de tempo e interage com `Building`;
> - `Elevator` altera o seu comportamento consoante o seu `ElevatorState`;
> - As estratégias de movimento (`Strategy`) decidem qual elevador atende um pedido;
> - A `GUI` e a `Console` interagem com a `Simulation` para renderizar a informação, respeitando agora o encapsulamento (Hide Delegate).

---

## ⚙️ 5. Execução e Testes

### 🧩 Requisitos:
- **JDK 17 ou superior**
- **Maven** (para build e dependências)
- **Bibliotecas JavaFX** (geridas pelo Maven)

### ▶️ Compilar o projeto:
```bash
mvn clean compile
```

### 🧪 Executar os testes unitários e de regressão:
```bash
mvn test
```

### 📖 Gerar Documentação JavaDoc (Obrigatório Fase 3):
Para gerar o site com a documentação técnica:
1. No IntelliJ: Menu `Tools` > `Generate JavaDoc`.
2. O resultado será guardado na pasta `javadoc/`.

### 🚀 5.1. Executar no Modo Consola
```bash
mvn exec:java -Dexec.mainClass="pt.ests.pa.MainConsole"
```

### 🎨 5.2. Executar no Modo Gráfico (JavaFX)
```bash
mvn exec:java -Dexec.mainClass="pt.ests.pa.MainJavaFX"
```

---

## 📅 6. Tabela de Estado do Projeto

| Tarefa | Descrição | Estado |
|--------|------------|---------|
| Simulação | Motor de tempo e lógica de movimento | ✅ Concluído |
| Padrões | Implementação de State, Strategy e Factory | ✅ Concluído |
| Visualização | Modo Consola funcional | ✅ Concluído |
| Visualização | Modo JavaFX funcional | ✅ Concluído |
| **Refactoring** | Limpeza de Smells (Fase 3) | ✅ Concluído |
| **JavaDoc** | Documentação completa da API (Fase 3) | ✅ Concluído |
| **Testes** | Validação de regressão pós-refactoring | ✅ Concluído |

---

## 🎨 7. Interface Gráfica (Mockups e Implementação)

As imagens abaixo representam a disposição visual implementada na interface JavaFX, permitindo acompanhar o movimento dos elevadores e o estado das filas.

![Mockup da Interface](mockup1.png)
![Mockup da Interface](mockup2.png)
![Mockup da Interface](mockup3.png)

---

## 👨‍💻 Autores

**Nomes:** Diogo Brito, Diogo Gomes e Rafael Junqueira  
**Unidade Curricular:** Programação Avançada (ESTS — 2025/26)  

**Fase:** 3 — Entrega Final

