from datetime import datetime, timedelta
from model.Caixa import Caixa
from model.Cliente import Cliente


class Agencia:
    def __init__(self):
        self.fila_normal = []
        self.fila_preferencial = []
        self.caixas = []

        for i in range(3):
            self.caixas.append(Caixa(False))

        for i in range(2):
            self.caixas.append(Caixa(True))

    def gerar_senha(self, preferencial):
        senha = len(self.fila_normal) + len(self.fila_preferencial) + 1
        cliente = Cliente(senha, preferencial, datetime.now())

        if preferencial:
            self.fila_preferencial.append(cliente)
        else:
            self.fila_normal.append(cliente)

        return senha

    def atender(self):
        for caixa in self.caixas:
            if caixa.atender(self.fila_preferencial, self.fila_normal):
                return True

        return False

    def verificar_tempo_medio(self):
        tempo_total = timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
        num_clientes = 0

        for fila in [self.fila_normal, self.fila_preferencial]:
            for cliente in fila:
                tempo_total += datetime.now() - cliente.hora_entrada
                num_clientes += 1

        tempo_medio = tempo_total / num_clientes if num_clientes > 0 else timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

        if tempo_medio > timedelta(microseconds=900) and len(self.caixas) < 5:
            self.caixas.append(Caixa(False))

        return tempo_medio
