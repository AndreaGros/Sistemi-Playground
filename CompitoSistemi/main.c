#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include "library.h"





/* TBD:
int controlla_lista_vuota(...)
nodo* NuovoNodo();
nodo* inserisciTesta(...)
nodo* inserisciPosizione(...,int pos)
nodo* eliminaNodo(...)
nodo* eliminaByPos(..., int pos);
nodo* aggiungiByPos(..., int pos);
nodo* aggiungiOrdinato(nodo *testa);
*/

char scriviMenu();

int main()
{
    nodo* head=NULL;
    char scelta;
    int x;
    head=caricaFile(head);
    do
    {
        scelta=scriviMenu();
        switch(scelta)
        {
        case 'A':
        case 'a':
            head = inserisciNodo(head);
            break;
        case 'B':
        case 'b':
            head = eliminaNodo(head);
            break;
        case 'C':
        case 'c':
            head = inserisciCoda(head);
            break;
        case 'D':
        case 'd':
            mostraLista(head);
            break;
        case 'E':
        case 'e':
            printf("Numero nodi: %d\n",contaNodi(head));
            break;
        case 'F':
        case 'f':
            trovaMaggiore(head);
            break;
        case 'G':
        case 'g':
            head=swap(head);
            break;
        case 'H':
        case 'h':
            head=ordinamento(head);
            break;
        case 'I':
        case 'i':
            do
            {
                printf("Inserisci x: ");
                scanf("%d",&x);
            }
            while(x<1);
            head=duplica(head, x);
            break;
        case 'L':
        case 'l':
            scriviFile(head);
            break;
        case 'M':
        case 'm':
            do{
                printf("Inserisci x: ");
                scanf("%d",&x);
            }while(x>contaNodi(head)-1);
            head=eliminaX(head, x);
            break;
        }

        fflush(stdin);
        getchar();
    }
    while(scelta!='Q'&&scelta!='q');

//    for(int i=0; i<1; i++)
//    {
//        head = inserisciNodo(head);
//    }
//    mostraLista(head);
//    printf("Numero nodi: %d\n",contaNodi(head));
//    //head = eliminaNodo(head);
//    //printf("Numero nodi: %d\n",contaNodi(head));
//    mostraLista(head);
//    head = inserisciCoda(head);
//    //mostraLista(head);
//    head = inserisciCoda(head);
//    mostraLista(head);
    return 0;
}


char scriviMenu()
{
    char sc;
    system("cls");
    printf("Libreria\n");
    printf("A. Inserisci nodo\n");
    printf("B. Elimina nodo\n");
    printf("C. Inserisci in coda\n");
    printf("D. Visualizza lista\n");
    printf("E. Conta nodi\n");
    printf("F. Trova maggiore\n");
    printf("G. Swap primi 2\n");
    printf("H. Ordinamento\n");
    printf("I. Duplica lista X volte\n");
    printf("L. Scrivi nel file\n");
    printf("M. Elimina in pos x\n");
    printf("Q. Esci\n");
    printf("Scelta -> ");
    fflush(stdin);
    sc=getchar();
    return sc;
}


