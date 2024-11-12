#ifndef LIBRARY_H_INCLUDED
#define LIBRARY_H_INCLUDED
#include <string.h>
#include <float.h>

#define MAX_AUTORE 50
#define MAX_TITOLO 100
#define ISBN_N 13
#define MAX_LINE 200

int id_Nodo=0;

typedef struct s_node
{
    int id_Nodo;
    char autore[MAX_AUTORE + 1];
    char titolo[MAX_TITOLO + 1];
    char ISBN[ISBN_N];
    int anno;
    char editore[MAX_AUTORE+1];
    float prezzo;
    struct s_node* next;
} nodo;


nodo* caricaFile(nodo* next)
{
    FILE *file = fopen("biblio - orig.csv", "r");
    char line[MAX_LINE+1];
    char *token;
    nodo* n_p;
    while (!feof(file))
    {
        fgets(line, MAX_LINE, file);
        n_p=(nodo*)malloc(sizeof(nodo));
        n_p->next=next;
        n_p->id_Nodo = id_Nodo++;
        token=strtok(line, "#");
        strcpy(n_p->autore,token);
        token=strtok(NULL, "#");
        strcpy(n_p->titolo,token);
        token=strtok(NULL, "#");
        strcpy(n_p->ISBN,token);
        token=strtok(NULL, "#");
        n_p->anno=atoi(token);
        token=strtok(NULL, "#");
        strcpy(n_p->editore,token);
        token=strtok(NULL, "\n");
        n_p->prezzo=atoi(token);
        next=n_p;
    }
    fclose(file);
    return next;
}

nodo* inserisciNodo(void* next)
{
    nodo* n_p;
    n_p=(nodo*)malloc(sizeof(nodo));
    n_p->next=next;
    n_p->id_Nodo = id_Nodo++;

    fflush(stdin);
    printf("Inserisci il titolo del libro(max %i carattere): ",(MAX_AUTORE));
    gets(n_p->titolo);

    fflush(stdin);
    printf("Inserisci l'autore del libro(max %i carattere): ", (MAX_TITOLO));
    gets(n_p->autore);

    fflush(stdin);
    printf("Inserisci ISBN(%i caratteri): ", (ISBN_N));
    gets(n_p->ISBN);

    printf("Inserisci l'anno di pubblicazione: ");
    scanf("%d",&(n_p->anno));

    fflush(stdin);
    printf("Inserisci l'editore(max %i caratteri): ", (MAX_AUTORE));
    gets(n_p->editore);

    printf("Inserisci il prezzo del libro: ");
    fflush(stdin);
    scanf("%f",&(n_p->prezzo));

    printf("Libro aggiunto correttamente\n");
    return n_p;
}


nodo* inserisciCoda(nodo* head)
{
    nodo* p_node = head;
    if(p_node == NULL)
    {
        return inserisciNodo(NULL);
    }
    while(p_node->next != NULL)
    {
        p_node = p_node->next;
    }
    p_node->next = inserisciNodo(NULL);
    return head;
}

nodo* eliminaNodo(nodo* node)
{
    printf("Sto cancellando il nodo %d \n",node->id_Nodo);
    nodo* aus = node->next;
    free(node);
    return aus;
}

int contaNodi(nodo* node)
{
    int i=0;
    while(node!=NULL)
    {
        node=node->next;
        i++;
    }
    return i;
}

void mostraLista(nodo* p_node)
{
    while(p_node != NULL)
    {
        printf("Libro n.%i: %s \n%s \n%i, %.2f euro\n", p_node->id_Nodo,
               p_node->titolo,
               p_node->autore,
               p_node->anno, p_node->prezzo);
        p_node=p_node->next;
    }
    printf("NULL \n");
}

void trovaMaggiore(nodo* node)
{
    nodo* aus;
    float massimo=FLT_MIN;
    while(node!=NULL)
    {
        if(node->prezzo>massimo)
        {
            massimo= node->prezzo;
            aus=node;
        }
        node=node->next;
    }
    printf("Libro n.%i: %s \n%s \n%i, %f euro\n", aus->id_Nodo,
           aus->titolo,
           aus->autore,
           aus->anno, aus->prezzo);
}

nodo* swap(nodo* current)
{
    if(contaNodi(current)<2)
        return current;
    nodo* aus = current->next;
    current->next = aus->next;
    aus->next = current;
    return aus;
}

nodo* ordinamento(nodo* head)
{
    nodo* current = head;
    nodo* prev;
    int swapped;
    int i, j, n;

    n=contaNodi(head);

    for (i = 0; i < n - 1; i++)
    {
        current = head;
        prev = NULL;
        swapped = 0;

        for (j = 0; j < n - 1 - i; j++)
        {
            if (current->id_Nodo > current->next->id_Nodo)
            {
                nodo* temp = swap(current);

                if (prev == NULL)
                {
                    head = temp;
                }
                else
                {
                    prev->next = temp;
                }
                prev = temp;
                swapped = 1;
            }
            else
            {
                prev = current;
                current = current->next;
            }
        }
        if (!swapped)
        {
            break;
        }
    }

    return head;


//    do {
//        swapped = 0;
//        current = head;
//
//        if (current != NULL && current->next != NULL && current->id_Nodo > current->next->id_Nodo) {
//            head = swap(current);  // Aggiorna la testa della lista
//            swapped = 1;
//        }
//
//        // Ciclo per il resto della lista
//        while (current != NULL && current->next != NULL && current->next->next != NULL) {
//            if (current->next->id_Nodo > current->next->next->id_Nodo) {
//                current->next = swap(current->next); // Aggiorna il puntatore a current->next con il risultato di swap
//                swapped = 1;
//            }
//            current = current->next;
//        }
//    } while (swapped);
//    return head;
}

nodo* duplica(nodo* head, int x)
{
    nodo* node = head;
    nodo* fine = head;
    int i, j, n;

    // Trova il numero di nodi attuali nella lista
    n = contaNodi(head);

    while (fine->next != NULL)
        fine = fine->next;

    for (i = 1; i < x; i++)
    {
        node = head;
        for (j = 0; j < n; j++)
        {
            nodo* duplicato = (nodo*)malloc(sizeof(nodo));
            duplicato->id_Nodo = id_Nodo++;
            duplicato->next = NULL;
            strcpy(duplicato->autore, node->autore);
            strcpy(duplicato->titolo, node->titolo);
            strcpy(duplicato->ISBN, node->ISBN);
            duplicato->anno = node->anno;
            strcpy(duplicato->editore, node->editore);
            duplicato->prezzo = node->prezzo;

            fine->next = duplicato;
            fine = duplicato;

            node = node->next;
        }
    }

    return head;
}

void scriviFile(nodo* node)
{
    FILE *file = fopen("biblio - orig.csv", "w");
    if (file == NULL)
    {
        printf("Errore nell'apertura del file!\n");
        return;
    }
    while (node != NULL)
    {
        fprintf(file, "%s#%s#%s#%d#%s#%.2f\n", node->titolo,
                node->autore,
                node->ISBN,
                node->anno,
                node->editore,
                node->prezzo);
        node = node->next;
    }
    fclose(file);
}

eliminaX(nodo* node, int x)
{
    nodo* prev;
    nodo* head=node;
    for(int i=0;i<x;i++){
        prev=node;
        node=node->next;
    }
    prev->next=node->next;
    free(node);
    return head;
}
#endif // LIBRARY_H_INCLUDED
