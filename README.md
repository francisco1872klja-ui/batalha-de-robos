🤖 Simulador de Batalha de Robôs (POO em Python)

Este projeto é um sistema de combate em turnos criado para exercitar e demonstrar os pilares da **Programação Orientada a Objetos (POO)** utilizando Python. 

O sistema conta com uma interface abstrata base (`Robo`) e diferentes subclasses que implementam mecânicas únicas de combate, cálculo de dano e esquiva.

---

## 🛠️ Conceitos de POO Aplicados

* **Abstração & Interfaces:** Uso do módulo `abc` (`ABC`, `@abstractmethod`) para definir um contrato padrão que obriga todas as subclasses de robôs a implementarem o método `receber_dano()`.
* **Polimorfismo:** Diferentes tipos de robôs recebem o mesmo tipo de ataque, mas reagem de formas totalmente distintas à mecânica de dano.
* **Herança:** Reutilização do construtor e comportamentos base através da classe `Robo` e da chamada `super()`.
* **Encapsulamento:** Proteção do atributo interno `_vida` para garantir integridade do estado do robô.
* **Type Hinting:** Garantia de tipagem do argumento `robo_inimigo: Robo` com validação de instância no método `lutar()`.

---

## 🎮 Classes e Mecânicas

### 1. `Robo` (Classe Abstrata Base)
* **Atributos:** `nome`, `_vida` (Padrão: 100).
* **Métodos:**
  * `lutar(robo_inimigo)`: Ataca uma instância de `Robo` e aplica o dano correspondente.
  * `receber_dano(valor)`: Método abstrato obrigatoriamente sobrescrito pelas filhas.

---

### 2. `RoboTank`
Especialista em resistência. Absorve parte do dano recebido, mas possui menos vida inicial e não consegue se esquivar.

* **Dano de Ataque:** `10`
* **Vida Inicial:** `55`
* **Passiva (Blindagem):** Reduz o dano recebido em **50%**.

---

### 3. `RoboRapido`
Um robô focado em agilidade. Possui alta probabilidade de desviar totalmente de um ataque, porém sofre dano severo se a esquiva falhar.

* **Dano de Ataque:** `15`
* **Vida Inicial:** `100`
* **Passiva (Esquiva):**
  * `30%` de chance de **esquivar** (dano zero).
  * Se a esquiva falhar, recebe o **dobro do dano** (`dano * 2`).

---

## 🚀 Como Executar

1. Certifique-se de ter o **Python 3.x** instalado.
2. Clone o repositório ou copie o código fonte.
3. Crie um script de teste (exemplo de uso):

```python
# Exemplo de combate no terminal
tank = RoboTank("Brutus")
rapido = RoboRapido("Flash")

print(tank)   # O Brutus(RoboTank) está com 55
print(rapido) # O Flash(RoboRapido) está com 100

# Rodada de ataque
tank.lutar(rapido)
rapido.lutar(tank)

print(tank)
print(rapido)
