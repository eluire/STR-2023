#include <cstdlib>   //qsort
#include  <time.h>   // clock(),time()
#include <stdio.h>   // printf()
#include <stdlib.h>  // exit()


//Vetores usados pelos métodos de ordenação
int *vetorQuickSort;
int *vetorBubbleSort;
int tamanho;

//Função usada pelo qsort para comparar dois numeros
int compare_ints( const void* a, const void* b ) {
	int* arg1 = (int*) a;
	int* arg2 = (int*) b;
	if( *arg1 < *arg2 ) return -1;
	else if( *arg1 == *arg2 ) return 0;
	else return 1;
}

//Algoritmos de ordenação bubble sort
void bubbleSort(int *vetor, int tamanho) {
	int aux;
	for (int i = 0; i < tamanho-1; i++) {
		for (int j = 0; j < tamanho-1; j++) {
			if (vetor[j] > vetor[j+1]) {
				aux = vetor[j];
				vetor[j] = vetor[j+1];
				vetor[j+1] = aux;
			}
		}
	}
}


//Observe que os números são gerados aleatoriamente baseados
//em uma semente. Se for passado a mesma semente, os 
//números aleatórios serão os mesmos
void criarVetor(int tamanhoVetor, int semente){
	srand (semente);
	vetorQuickSort = new int[tamanhoVetor];
	vetorBubbleSort = new int[tamanhoVetor];
	for (int i=0;i<tamanhoVetor;i++){
		vetorQuickSort[i] =  rand()%100000;
        vetorBubbleSort[i] = vetorQuickSort[i]; // utilizar os mesmos valores
		//vetorBubbleSort[i] = rand()%100000;
	}
}



int main ()
{
	//Tamanho do vetor
	int n = 100000;
	//Criar vetor com elementos aleatorios[0,100000] 
	criarVetor(n,23);
	
	clock_t inicio_q, fim_q, inicio_b, fim_b;
	double diferenca_q, diferenca_b;
	
	//Ordenar utilizando quickSort
	
	inicio_q = clock();
	
	qsort (vetorQuickSort, n, sizeof(int), compare_ints);
	
	fim_q = clock();
	
	diferenca_q = (double)(fim_q - inicio_q) / CLOCKS_PER_SEC * 1000.0; // Calcular a diferença em milissegundos
	
	printf("QuickSort Demorou %lfms pra ordenar!\n", diferenca_q);
	
	
	//Ordenar utilizando bubleSort
	
	inicio_b = clock();
	
	bubbleSort(vetorBubbleSort,n);
	
	fim_b = clock();
	
	diferenca_b = (double)(fim_b - inicio_b) / CLOCKS_PER_SEC * 1000.0; // Calcular a diferença em milissegundos
	
	printf("BubbleSort Demorou %lfms pra ordenar!\n", diferenca_b);
	
    	printf("terminou");
	
	exit(0);
}

