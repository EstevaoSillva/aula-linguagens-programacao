#include <iostream>
#include <string>

using namespace std;

int main(){
    string nome, sobrenome, tamanho;
    cout << "Digite seu nome: ";
    cin >> nome;
    tamanho = nome.size()-1;
    cout << "Digite seu Sobrenome: ";
    cin >> sobrenome;

    cout << sobrenome << "," << nome[0] << tamanho << endl;
    return 0;
}