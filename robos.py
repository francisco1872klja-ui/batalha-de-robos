from abc import ABC,abstractclassmethod
from random import randint

class Robo(ABC):
    """Class ROBO: contrati para as outras classes"""

    def __init__(self, nome):
        self.nome = nome
        self._vida = 100


    def lutar(self,robo_inimigo:Robo):
        if not isinstance(robo_inimigo,Robo):
            raise ValueError(f"O inimigo não é um robo!")
        if self._vida == 0:
            print(f"{self.nome}({self.__class__.__name__}) Morto!")
            return
        robo_inimigo.receber_dano(type(self).dano)

    @abstractclassmethod
    def receber_dano(self,valor:int):
        pass
    
    def __str__(self):
        return f"O {self.nome}({self.__class__.__name__}) está com {self._vida}"

class RoboTank(Robo):
    """Cria um robotank ele recebe menos dano mas n tem esquiva!"""
    dano = 10

    def __init__(self, nome):
        super().__init__(nome)
        self._vida = 55
    
    def receber_dano(self, valor):
        self._vida -= int(valor*0.5)

        if self._vida < 0:
            self._vida = 0

class RoboRapido(Robo):
    """Cria um RoboRapido ele tem esquiva mas se falhar toma o dobro do dano!"""

    dano = 15
    chance_esquiva = 0.30

    def __init__(self, nome):
        super().__init__(nome)

    def esquiva(self):
        sorte = randint(1,100)

        if 1< sorte < 100*RoboRapido.chance_esquiva:
            return True
        else:
            return False

    def receber_dano(self, valor):
        if self.esquiva():
            print(f"{self.nome} esquivou!")
        else:
            self._vida -= valor*2

        if self._vida < 0:
            self._vida = 0
