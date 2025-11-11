#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

void bubblesort(int arr[], int n) {  
    int i, j, temp;
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void bubbleSortdec(int arr[], int n) { 
    int i, j, temp;
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] < arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void printarray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[] = {4, 6, 2, 5, 3, 1, 5, 3, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Original array: ");
    printarray(arr, n);

    if (fork() == 0) {
        // Child process → Descending
        printf("\nChild process (PID: %d)\n", getpid());
        int childArr[n];
        for (int i = 0; i < n; i++) childArr[i] = arr[i]; // Copy array
        bubbleSortdec(childArr, n);
        printf("Child sorted (Descending): ");
        printarray(childArr, n);
    } else {

        printf("\nParent process (PID: %d)\n", getpid());
        int parentArr[n];
        for (int i = 0; i < n; i++) parentArr[i] = arr[i];
        bubblesort(parentArr, n);
        printf("Parent sorted (Ascending): ");
        printarray(parentArr, n);
    }

    return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    pid_t child_pid = fork();

    if (child_pid > 0) {
        // Parent process
        printf("Parent process (PID: %d) sleeping for 10 seconds...\n", getpid());
        // pid_t wait(int *status);
	    sleep(5);  
        printf("Process table snapshot:\n");
        system("ps -axj | tail");  
        sleep(5);  
        printf("Parent process exiting.\n");
    }
    else if (child_pid == 0) {
        // Child process
        printf("Child process (PID: %d) exiting now...\n", getpid());
        exit(0);
    }
    else {
        // Fork failed
        perror("fork failed");
        return 1;
    }

    return 0;
}

#include <stdio.h>
#include <unistd.h>
#include<sys/types.h>
int main(){
	int pid=fork();
	if (pid>0){
		printf("\nParent process runnig.........\n");
		printf("parent process id  %d\n",getpid());
		printf("child process id %d\n",pid);
	}
	else{
		sleep(10);
		printf("\nchild process running..........\n");
		printf("\nchild process id %d\n",getpid());
		printf("parent processs id %d\n",getppid());
	}
	return 0;
}
