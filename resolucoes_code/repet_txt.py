# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

class Repeticao():
    def __init__(self, palavra, numero):
        self.palavra = palavra
        self.numero = numero

    def laco(self):
        for _ in range(self.numero):
            print(self.palavra + ' ')

ins = Repeticao(str(input("Insira uma palavra: ")), int(input("Insira um número: ")))
ins.laco()