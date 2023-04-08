from model.Agencia import Agencia
from datetime import timedelta


def main():
    agencia = Agencia()

    while True:
        print("1 - Gerar senha preferencial")
        print("2 - Gerar senha normal")
        print("3 - Atender cliente")
        print("4 - Sair")

        opcao = int(input("Digite uma opção: "))

        if opcao == 1:
            senha = agencia.gerar_senha(True)
            print("Senha preferencial gerada: ", senha)
        elif opcao == 2:
            senha = agencia.gerar_senha(False)
            print("Senha normal gerada: ", senha)
        elif opcao == 3:
            atendido = agencia.atender()

            if atendido:
                print("Cliente sendo atendido")
            else:
                print("Todos os caixas estão ocupados")

            tempo_medio = agencia.verificar_tempo_medio()

            if tempo_medio > timedelta(microseconds=900):
                print("Tempo médio de espera: ", tempo_medio)
        elif opcao == 4:
            print("Obrigado por utilizar nossos Serviços.")
            break
        else:
            print("Opção inválida.")


if __name__ == '__main__':
    main()
