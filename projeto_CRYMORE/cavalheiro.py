from guerreiro import Guerreiro 
import random

obj1=Guerreiro()
class cavalheiro(Guerreiro):

    def __init__(self):
        super().__init__()
        self.armardura=0
        self.arma=""

    def ataque_podereso(self):
        self.dano=obj1.ataque+random.randint(5,20)
        return self.dano
        
