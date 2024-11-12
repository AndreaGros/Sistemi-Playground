#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int id_Nodo=0;

typedef struct s_node
{
    int id_Nodo;
    char autore[50 + 1];
    char titolo[100 + 1];
    struct s_node* next;
} nodo;

nodo* inserisciNodo(void* next);
void inserisciDati(nodo* node);

int main()
{
    nodo* head=NULL;
    head=inserisciNodo(head);
    inserisciDati(head);
    printf("Autore: %s\nTitolo: %s", head->autore, head->titolo);
    return 0;
}

nodo* inserisciNodo(void* next){
    nodo* n_p;
    n_p=(nodo*)malloc(sizeof(nodo));
    n_p->next=next;
    n_p->id_Nodo = id_Nodo++;
    return n_p;
}

void inserisciDati(nodo* node){
    strcpy(node->autore,"Andrea");
    strcpy(node->titolo,"Come diventare ricco");
}
