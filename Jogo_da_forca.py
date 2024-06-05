import os

# Lista para armazenar as letras adivinhadas e suas cores
letras = []

# Solicita o nome do jogador que vai inventar a palavra
print('Jogador que vai inventar a palavra digite seu nome')
nome_jogador_inventar_palavra = input('Informe seu nome: ').capitalize().strip()

# Solicita o nome do jogador que vai descobrir a palavra
print('Jogador que vai descobrir a palavra digite seu nome')
nome_jogador_descobrir_palavra = input('Informe seu nome: ').capitalize().strip()

# Limpa o terminal 
os.system('cls')

# Solicita a palavra ao jogador que inventa a palavra
print(f'\033[33m{nome_jogador_inventar_palavra}\033[39m, é a sua vez')
word = input('Digite uma palavra:').lower().strip()

# Limpa o terminal novamente
os.system('cls')

# Anuncia a vez do jogador que vai descobrir a palavra
print(f'\033[34m{nome_jogador_descobrir_palavra}\033[39m, é a sua vez')
print('Você tem 8 tentativas')

# Loop para 8 tentativas de descobrir a palavra
for _ in range(8):
    os.system('cls')
    letras_formatadas = ' '.join(letras)
    print(f'As letras que já foram são essas: {letras_formatadas}')
    descobrir_letra = input(f'\033[34m{nome_jogador_descobrir_palavra}\033[39m, informe uma letra: ').lower().strip()

    if descobrir_letra in word:
        letras.append(f'\033[32m{descobrir_letra}\033[39m')  # Adiciona a letra em verde
        print(f'\033[32m{descobrir_letra}\033[39m está na palavra')
    else:
        letras.append(f'\033[31m{descobrir_letra}\033[39m')  # Adiciona a letra em vermelho
        print(f'\033[31m{descobrir_letra}\033[39m não está na palavra')

print(f'A palavra a ser descoberta era: {word}')

