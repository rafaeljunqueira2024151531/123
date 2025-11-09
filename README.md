# 🏢 Simulador de Elevadores em Prédio Virtual
### Programação Avançada 2025/26 — Fase 1 (Modelo do Simulador)

---

## 📘 1. Descrição do Projeto
Este projeto implementa o **modelo base** de um simulador de elevadores, que representa o funcionamento interno de um edifício com pisos, elevadores e passageiros com diferentes prioridades.

A **Fase 1** centra-se na modelação das entidades principais e nas suas interações, sem interface gráfica.  
As principais funcionalidades desta fase incluem:

- Criação de edifícios com número variável de pisos e elevadores;  
- Geração aleatória de passageiros com diferentes tipos e prioridades;  
- Simulação do embarque e desembarque de passageiros nos elevadores;  
- Estruturas de dados genéricas (`Queue`, `PriorityQueue`, `ArrayPriorityQueue`);  
- Testes unitários para validar o comportamento do modelo.

---

## 🧩 2. Estrutura do Projeto

```
src/
 ├── main/
 │   └── java/
 │       └── pt/ests/pa/
 │            ├── adt/               → Estruturas de dados genéricas (Queue, PriorityQueue)
 │            ├── buildings/         → Classe Building (edifício com pisos e elevadores)
 │            ├── elevators/         → Classe Elevator (gestão de passageiros e destinos)
 │            ├── floors/            → Classe Floor (fila de passageiros)
 │            └── passengers/        → Passenger, PassengerGenerator, PassengerType
 │
 └── test/
     └── java/
         └── pt/ests/pa/
              ├── adt/ArrayPriorityQueueTest.java
              ├── buildings/BuildingTest.java
              ├── elevators/ElevatorTest.java
              ├── floors/FloorTest.java
              └── passengers/
                   ├── PassengerTest.java
                   └── PassengerGeneratorTest.java
```

---

## 🧱 3. Diagrama UML de Classes

O modelo segue uma arquitetura modular, organizada por pacotes.  
O diagrama abaixo representa as relações entre as classes principais e as estruturas ADT utilizadas.

![Diagrama UML](uml_diagrama.png)

> **Resumo das Relações:**
> - `Building` contém múltiplos `Elevator` e `Floor`;  
> - `Elevator` e `Floor` gerem listas de `Passenger`;  
> - `PassengerGenerator` cria novos `Passenger` aleatoriamente;  
> - `ArrayPriorityQueue` implementa `PriorityQueue`, baseada em `Queue<T>`.

---

## ⚙️ 4. Execução e Testes

### 🧩 Requisitos:
- **JDK 17 ou superior**
- **Maven** (para build e testes)
- **JUnit 5** (para testes unitários)

### ▶️ Compilar o projeto:
```bash
mvn clean compile
```

### 🧪 Executar os testes unitários:
```bash
mvn test
```

---

## 📅 5. Estado da Fase 1

| Tarefa | Descrição | Estado |
|--------|------------|---------|
| Modelo de dados | Classes `Building`, `Elevator`, `Floor`, `Passenger`, `PassengerGenerator` | ✅ Concluído |
| Estruturas de dados (ADT) | `Queue`, `PriorityQueue`, `ArrayPriorityQueue` | ✅ Concluído |
| Testes unitários | Validação de comportamento das classes principais | ✅ Concluído |
| Documentação (README + Javadoc) | Organização e explicação da arquitetura | ✅ Concluído |

---

## 🎨 6. Mockup da Interface (Pré-visualização da Fase 2)

O seguinte mockup representa a futura interface gráfica da aplicação (Fase 2),  
onde será possível visualizar o movimento dos elevadores e o estado dos pisos.

![Mockup da Interface](mockup1.png)
![Mockup da Interface](mockup2.png)
![Mockup da Interface](mockup3.png)

> O mockup foi criado para ilustrar a disposição dos elevadores, filas de passageiros e indicadores de estado.  
> A implementação funcional será desenvolvida na **Fase 2** do projeto.

---

## 👨‍💻 Autores

**Nomes:** Diogo Brito, Diogo Gomes e Rafael Junqueira  
**Unidade Curricular:** Programação Avançada (ESTS — 2025/26)  
**Fase:** 1 — Implementação do Modelo do Simulador  