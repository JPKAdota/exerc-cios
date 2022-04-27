class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.nome = nome

    def envelhecer(self):
        if self.idade < 21:
          self.altura += 0.5
          self.idade += 1

carlos = Pessoa('Carlos', 2, 12, 80)

for _ in range(22):
    carlos.envelhecer()
    print(f'Idade do {carlos.nome} é: {carlos.idade} anos e sua altura é {carlos.altura} cm')