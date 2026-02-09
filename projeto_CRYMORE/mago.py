from guerreiro import Guerreiro

class Mago(Guerreiro):

    def __init__(self):
        super().__init__()
        self.mana=0
        self.grimorio=""

    def lancar_feitico(self):
        self.mana=self.mana-50
        self.dano=self.ataque
        