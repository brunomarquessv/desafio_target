# Desafio 02
# A funçao sequencia_fibonacci verifica se um número pertence ou não a sequência de fibonacci.
def sequencia_fibonacci(numero):
    # A função inicia indicando os dois primeiros números da sequência.
    a, b = 0, 1
    # Verifica se o número é 0 ou 1
    if numero == 0 and numero == 1:
        print(f"O número ({numero} pertence a sequência de fibonacci.")
        return 
    
    # Este looping calcula a sequencia ate que seja encontrado um numero maior que o que foi informado.
    while b < numero:
        a, b = b, a + b

    # Neste trecho acontece a verificação final se o número pertence ou não a sequencia.
    if b == numero: 
        print(f"O número ({numero}) pertence a sequência de fibonacci.")
    else: 
        print(f"O número ({numero}) não pertence a sequência de fibonacci.")
    
# Saída do usuário
numero = int(input("Informe um número: "))

# Invocação da função
sequencia_fibonacci(numero)