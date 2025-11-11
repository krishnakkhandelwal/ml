#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <unistd.h>
#define MAX 20

// filedes[0]: read
// filedes[1]: write

int main() {
    int filedes[2], n;
    char string[MAX], line[MAX];
    pid_t pid;

    printf("Enter string for parent: ");
    fflush(stdin);
    fgets(string, MAX, stdin);

    // if returns -1 -> fail
    if (pipe(filedes) < 0) {
        printf("\nPipe creation Error!");
        exit(0);
    }
    if ((pid=fork()) < 0) {
        printf("Fork error\n");
        exit(0);
    }
    if (pid > 0) {
        close(filedes[0]);
        write(filedes[1], string, MAX);
    }
    if (pid == 0) {
        close(filedes[1]);
        n = read(filedes[0], line, MAX);
        line[n] = '\0';
        printf("Line read by child: %s\n", line);
    }
    exit(0);
}

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#define MAX 20

int main() {
    int filedes1[2], filedes2[2], n;
    char string[MAX], line[MAX];
    pid_t pid;

    // Create both pipes
    if (pipe(filedes1) < 0 || pipe(filedes2) < 0) {
        printf("\nPipe creation Error!");
        exit(0);
    }

    if ((pid = fork()) < 0) {
        printf("Fork error\n");
        exit(0);
    }

    if (pid > 0) {  //  Parent 
        close(filedes1[1]); 
        close(filedes2[0]); 

        //  Read from child
        n = read(filedes1[0], line, MAX);
        line[n] = '\0';
        printf("Parent read from child: %s\n", line);

        //  Write to child
        printf("Enter string for parent to send: ");
        fflush(stdin);
        fgets(string, MAX, stdin);
        write(filedes2[1], string, MAX);

        close(filedes1[0]);
        close(filedes2[1]);
    }
    else {
        // Child
        close(filedes1[0]); 
        close(filedes2[1]); // close write end of parent->child

        // Child writes first
        printf("Enter string for child to send: ");
        fflush(stdin);
        fgets(string, MAX, stdin);
        write(filedes1[1], string, MAX);

        // Then child reads response
        n = read(filedes2[0], line, MAX);
        line[n] = '\0';
        printf("Child read from parent: %s\n", line);

        close(filedes1[1]);
        close(filedes2[0]);
    }

    exit(0);
}
