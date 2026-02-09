class Guerreiro:

    def __init__(self):
        self.nome=""
        self.nivel=0
        self.hp=0
        self.ataque=0
    
    def apresentar(self):
        print (f"""
-------------------------//---------------------------               
              INFORMAÇÕES DO GUERREIRO
              
        NOME:{self.nome}
        NIVEL{self.nivel}
        HP:{self.hp}
        ATAQUE:{self.ataque}

-------------------------//---------------------------                  
              """)
    
    