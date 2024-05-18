# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!
class Lendo_Dados():
    def __init__(self, dado1, dado2):
        self.dado1 = dado1
        self.dado2 = dado2

    def __str__(self):
        return self.dado1 + ' ' + self.dado2

print(Lendo_Dados(str(input("Insira um dado: ")), str(input("Insira o segundo dado: "))))