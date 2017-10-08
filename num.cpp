#include <iostream>
#include <chrono>
#include <fstream>
#include <time.h>
#include <thread>
#include <math.h>
#include <pthread.h>


using namespace std;

/**
	Authors: Paulo Victor & Rodrigo Laffayette

	Compiling: g++ -std=c++11 -std=c++11 -pthread num.cpp -o exe


	Executing ex.: ./exe  512     64
					  (matrix) (threads)

	execucao com 1 parametro = calculo normal
	execucao com 2 parametros = calculo com n threads

*/



/***
	Funcao que calcula a multiplicacao da matriz atraves de threads ( cada thread tem uma parte da interacao mais exterior)


	@param current : especifica qual a thread atual que esta sendo iterada na criacao
	@param threads : especifica a quantidade de threads passadas como parametro na inicializacao do programa (argv[2])
*/
void calcThreadMatrix( int row, int col, int** matrizA,int** matrizB , int** matrizC,int current,int threads ){
	
	for(int i=(current*row)/threads ;i< (row*(current+1))/threads;i++){
		for(int j=0 ;j< row; j++){
			for(int k=0 ;k< row; k++){

				matrizC[i][j] += matrizA[i][k] * matrizB[k][j];

			}
		}
	}

	//return matrizC;
}
/***
	Funcao que calcula a multiplicacao de matriz comum
*/
void calcMatrix( int row, int col, int** matrizA,int** matrizB ,int** matrizC){

	for(int i=0;i<row;i++){
		for(int j=0;j<col;j++){
			for(int k=0;k<col;k++){

				matrizC[i][j] += matrizA[i][k] * matrizB[k][j];

			}
		}
	}

	//return matrizC;

}



int main(int argc , char* argv[]){


	chrono::high_resolution_clock::time_point t1 = chrono::high_resolution_clock::now();

	if(argc < 2){
		std::cerr<<"nao foi informado a quantidade suficiente de parametros"<<endl;
		return(false);
	}
	
	
	string strSize = argv[1]; //argumento 1 em forma de string
	int size = stoi(argv[1]); //argumento 1 em forma de inteiro

	//string file_name = "Matrizes/A4x4.txt";
	string file_name = "Matrizes/A" + strSize+"x"+strSize+".txt";


	ifstream arquivo;
	arquivo.open(file_name);

	int row=size,col=size;


	//nt matrizA[row][col];
	int** matrizA;
	matrizA = new int*[row];
	for (int i = 0; i < row; ++i)
    	matrizA[i] = new int[col];

	

	if(arquivo.is_open()){
		while(!arquivo.eof()){
			
			arquivo >> row;
			
			arquivo >> col;
			
			for(int x=0;x<row;x++){
				for(int y=0;y<col;y++){
					arquivo >> matrizA[x][y];
				}
			}
			
		}
	}
	arquivo.close();


	///////////////////////////////////////////////////////Partes relevantes a matriz B
	
	//string file_name2 = "Matrizes/B4x4.txt";
	string file_name2 = "Matrizes/B" + strSize+"x"+strSize+".txt";
	ifstream arquivo2;
	arquivo2.open(file_name2);

	//int matrizB[row][col];
	int** matrizB;
	matrizB = new int*[row];
	for (int i = 0; i < row; ++i)
    	matrizB[i] = new int[col];



	if(arquivo2.is_open()){
		while(!arquivo2.eof()){
			
			arquivo2 >> row;
			
			arquivo2 >> col;
			
			for(int x=0;x<row;x++){
				for(int y=0;y<col;y++){
					arquivo2 >> matrizB[x][y];
				}
			}
			
		}
	}
	arquivo2.close();
	///////////////////////////////////////////////Parte relevante a multiplicacao da matriz
	

	int** matrizC = new int*[row];
	for (int i = 0; i < row; ++i)
    	matrizC[i] = new int[col];
   
    //Zerando os elementos dentro da matriz
   	for(int x=0;x<row;x++){
		for(int y=0;y<col;y++){
			matrizC[x][y] = 0;
		}
	}	



	if(argc > 2){ //caso haja mais de 2 argumentos ao executar o programa utilizar as threads
		thread threads[stoi(argv[2])];
		for(int i=0;i<stoi(argv[2]); i++){

			threads[i] = thread( calcThreadMatrix, row, col, matrizA, matrizB,(int**)matrizC,i, stoi(argv[2]));
		}
		
		for(int i=0;i<stoi(argv[2]); i++){
			threads[i].join();
		}

	}
	else{ //caso nao haja mais de 2 argumentos, calcular sem threads
		calcMatrix(row,col,matrizA,matrizB,(int**)matrizC); 
	}


	chrono::high_resolution_clock::time_point t2 = chrono::high_resolution_clock::now();


	//imprimindo matriz resultante
	//cout<<endl;
	/*for(int x=0;x<row;x++){
		for(int y=0;y<col;y++){
			cout<<" "<<matrizC[x][y];
		}
		cout<<endl;
	}*/

	ofstream results;
	results.open("Res/C"+strSize+"x"+strSize+".txt");
	for(int x=0;x<row;x++){
		for(int y=0;y<col;y++){
			results<<" "<<matrizC[x][y];
		}
		results<<endl;
	}
	results.close();

	chrono::duration<double> final = t2- t1;
	
	//cout<< endl<<"operacao demorou "<< final.count() << " segundos"<<endl;
	cout<<final.count()<<endl;

}