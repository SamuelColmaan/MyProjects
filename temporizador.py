import time

def temporizador(segundos):
    for i in range(segundos, 0, -1):
        print(i)
        time.sleep(1)
    print("Tempo esgotado!")

# Solicita que o usuário insira a quantidade de segundos desejada
try:
    segundos = int(input("Por favor, insira a quantidade de segundos para o temporizador: "))
    if segundos <= 0:
        raise ValueError
except ValueError:
    print("Por favor, insira um valor inteiro positivo para os segundos.")
else:
    print(f"Temporizador iniciado para {segundos} segundos.")
    temporizador(segundos)
