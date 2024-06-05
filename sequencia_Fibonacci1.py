# Definir os primeiros dois termos da sequência
Fibonacci1 = 34
Fibonacci2 = 55

# Inicializar uma lista para armazenar a sequência de Fibonacci
FibonacciSequencia = []

# Adicionar os primeiros dois termos à lista
FibonacciSequencia.append(Fibonacci1)
FibonacciSequencia.append(Fibonacci2)

# Iterar para calcular os próximos 998 termos
for i in range(1, 999):
    # Calcular o próximo termo como a soma dos dois termos anteriores
    ProximoTermo = Fibonacci1 + Fibonacci2
    
    # Atualizar os termos anteriores
    Fibonacci1 = Fibonacci2
    Fibonacci2 = ProximoTermo
    
    # Adicionar o novo termo à lista
    FibonacciSequencia.append(ProximoTermo)

# Exibir os termos da sequência de Fibonacci
for termo in FibonacciSequencia:
    print(termo)
