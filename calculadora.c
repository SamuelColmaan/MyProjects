#include <stdio.h>

int main() {
    int num1, num2;
    char c;

    // Loop para garantir que o usuário insira um número válido para num1
    while (1) {
        printf("Digite o primeiro numero: ");
        if (scanf("%d", &num1) == 1) {
            break;  // Saia do loop se a entrada for válida
        } else {
            printf("Erro: Entrada invalida. Por favor, digite um numero.\n");
            // Limpa a entrada inválida
            while ((c = getchar()) != '\n' && c != EOF);
        }
    }

    // Loop para garantir que o usuário insira um número válido para num2
    while (1) {
        printf("Digite o segundo numero: ");
        if (scanf("%d", &num2) == 1) {
            break;  // Saia do loop se a entrada for válida
        } else {
            printf("Erro: Entrada invalida. Por favor, digite um numero.\n");
            // Limpa a entrada inválida
            while ((c = getchar()) != '\n' && c != EOF);
        }
    }

    int soma = num1 + num2;
    int subtracao = num1 - num2;
    int multiplicacao = num1 * num2;
    double divisao;

    // Verifica se num2 é zero antes de realizar a divisão
    if (num2 != 0) {
        divisao = (double)num1 / num2;
        printf("O resultado da divisao entre os numeros %d e %d eh: %.2lf\n", num1, num2, divisao);
    } else {
        printf("Erro: Divisao por zero!\n");
    }

    printf("O resultado da soma entre os numeros %d e %d eh: %d\n", num1, num2, soma);
    printf("O resultado da subtracao entre os numeros %d e %d eh: %d\n", num1, num2, subtracao);
    printf("O resultado da multiplicacao entre os numeros %d e %d eh: %d\n", num1, num2, multiplicacao);

    return 0;
}
