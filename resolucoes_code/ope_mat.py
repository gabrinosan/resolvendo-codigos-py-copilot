# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
class Lendo_Num():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def soma(self):
        print(f"A soma de {self.num1} + {self.num2} é {self.num1 + self.num2}")

    def sub(self):
        print(f"A subtração de {self.num1} - {self.num2} é {self.num1 - self.num2}")
        
    def div(self):
        if self.num2 != 0: print(f"A divisão de {self.num1} / {self.num2} é {self.num1 / self.num2}")
        else: print("O segundo número precisa ser diferente de zero")

    def mult(self):
        print(f"A multiplicação de {self.num1} x {self.num2} é {self.num1 * self.num2}")

ins = Lendo_Num(float(input("Insira um número: ")), float(input("Insira o segundo número: ")))

for nome, operador in vars(Lendo_Num).items():
    if callable(operador) and not nome.startswith('__'):
        operador(ins)