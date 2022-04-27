class BombaCombustivel:
    def __init__(self, combustivel_tipo: str, valor_litro: float, quantidade_combustivel: float):
        self.quantidade_combustivel = quantidade_combustivel
        self.valor_litro = valor_litro
        self.combustivel_tipo = combustivel_tipo

    def abastecer_por_valor(self, valor: float):
        litros_abastecidos = valor / self.valor_litro
        self._apresentar_abastecimento_se_possivel(litros_abastecidos, valor)

    def _apresentar_abastecimento_se_possivel(self, litros_abastecidos: float, valor: float):
        if litros_abastecidos > self.quantidade_combustivel:
            print('Não é possivel abastecer')
        else:
            self.quantidade_combustivel -= litros_abastecidos
            print(f'Foram abastecidos: {litros_abastecidos: .2f} litros a um valor de R$ {valor: .2f}')
            print(f'Sobraram na bomba {self.quantidade_combustivel: .2f} litros de {self.combustivel_tipo}')

    def abastecer_por_litros(self, litros_abastecidos: float):
        valor = litros_abastecidos * self.valor_litro
        self.quantidade_combustivel -= litros_abastecidos
        self._apresentar_abastecimento_se_possivel(litros_abastecidos, valor)



bomba = BombaCombustivel('Gasolina', 4.59, 100.0)

bomba.abastecer_por_valor(100)
bomba.abastecer_por_litros(50)
