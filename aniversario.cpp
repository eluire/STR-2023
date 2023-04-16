#include <stdio.h>
#include <time.h>

int main() {
    // Pedir ao usuário para inserir a data de nascimento
    int dia, mes, ano;
    printf("Insira a sua data de nascimento (DD/MM/AAAA): ");
    scanf("%d/%d/%d", &dia, &mes, &ano);
    
    // Obter a hora atual e a hora de nascimento em segundos
    time_t agora = time(NULL);
    struct tm nascimento = {0};
    nascimento.tm_year = ano - 1900;
    nascimento.tm_mon = mes - 1;
    nascimento.tm_mday = dia;
    time_t nascimento_segundos = mktime(&nascimento);
    
    // Calcular a diferença em segundos entre a hora atual e a hora de nascimento
    double segundos_vida = difftime(agora, nascimento_segundos);
    
    // Exibir o resultado ao usuário
    printf("Você tem %.0f segundos de vida!\n", segundos_vida);
    
    return 0;
}
