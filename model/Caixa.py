from datetime import datetime


class Caixa:
    def __init__(self, preferencial):
        self.preferencial = preferencial
        self.livre = True
        self.cliente_atual = None

    def atender(self, fila_preferencial, fila_normal):
        if not self.livre:
            return False

        fila = fila_preferencial if self.preferencial else fila_normal

        if len(fila) == 0:
            return False

        self.cliente_atual = fila.pop(0)
        self.livre = False
        self.cliente_atual.hora_atendimento = datetime.now()

        return True

    def liberar(self):
        if self.livre:
            return False

        self.livre = True
        self.cliente_atual = None

        return True
