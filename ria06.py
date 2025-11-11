#include <semaphore.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

sem_t mut1;
sem_t wrt;
int sharedvar = 99;
int readcount = 0;

void* writer(void* arg) {
    int id = *(int*)arg;
    printf("\nWriter %d is trying to enter CS", id);

    sem_wait(&wrt);
    printf("\nWriter %d entered CS", id);
    
    sharedvar++;
    printf("\nWriter %d updated shared variable to %d", id, sharedvar);
    
    sleep(1);
    sem_post(&wrt);
    printf("\nWriter %d left CS", id);
    return NULL;
}

void* reader(void* arg) {
    int id = *(int*)arg;

    sem_wait(&mut1);
    readcount++;
    if (readcount == 1)
        sem_wait(&wrt);
    sem_post(&mut1);

    printf("\nReader %d is reading sharedvar = %d", id, sharedvar);
    sleep(1);

    sem_wait(&mut1);
    readcount--;
    if (readcount == 0)
        sem_post(&wrt);
    sem_post(&mut1);

    printf("\nReader %d finished reading", id);
    return NULL;
}

int main() {
    int n, i;
    printf("Enter the number of readers and writers: ");
    scanf("%d", &n);

    pthread_t readers[n], writers[n];
    int ids[n];

    sem_init(&mut1, 0, 1);
    sem_init(&wrt, 0, 1);

    for (i = 0; i < n; i++) {
        ids[i] = i + 1;
        pthread_create(&writers[i], NULL, writer, &ids[i]);
        pthread_create(&readers[i], NULL, reader, &ids[i]);
    }

    for (i = 0; i < n; i++) {
        pthread_join(writers[i], NULL);
        pthread_join(readers[i], NULL);
    }

    return 0;
}
