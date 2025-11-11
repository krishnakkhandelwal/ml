#include <stdio.h>

int main() {
    int n, m;
    printf("Enter number of processes: ");
    scanf("%d", &n);
    printf("Enter number of resource types: ");
    scanf("%d", &m);

    int Available[m];
    int Max[n][m];
    int Allocation[n][m];
    int Need[n][m];
    printf("Enter Available resources :\n");
    for (int j = 0; j < m; j++) {
        scanf("%d", &Available[j]);
    }

    printf("Enter Max matrix (%d rows, %d columns):\n", n, m);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &Max[i][j]);
        }
    }

    printf("Enter Allocation matrix (%d rows, %d columns):\n", n, m);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &Allocation[i][j]);
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            Need[i][j] = Max[i][j] - Allocation[i][j];
        }
    }

    printf("\nProcess\tAlloc\tMax\tNeed\n");
    printf("\t");
    for (int k = 0; k < m; k++) printf("A B C\t"); 
    printf("\n");

    for (int i = 0; i < n; i++) {
        printf("P%d\t", i);
        for (int j = 0; j < m; j++) printf("%d ", Allocation[i][j]);
        printf("\t");
        for (int j = 0; j < m; j++) printf("%d ", Max[i][j]);
        printf("\t");
        for (int j = 0; j < m; j++) printf("%d ", Need[i][j]);
        printf("\n");
    }

    printf("\nAvailable resources:\n");
    printf("A B C\n"); 
    for (int j = 0; j < m; j++) printf("%d ", Available[j]);
    printf("\n");

    //SAFETY ALGORITHM
   
    int finish[n], safeSeq[n], work[m];
    for (int j = 0; j < m; j++)
        work[j] = Available[j];

    for (int i = 0; i < n; i++)
        finish[i] = 0;

    int count = 0;
    while (count < n) {
        int found = 0;
        for (int i = 0; i < n; i++) {
            if (finish[i] == 0) {
                int flag = 0;
                for (int j = 0; j < m; j++) {
                    if (Need[i][j] > work[j]) {
                        flag = 1;
                        break;
                    }
                }
                if (flag == 0) {
                    for (int j = 0; j < m; j++)
                        work[j] += Allocation[i][j];

                    safeSeq[count++] = i;
                    finish[i] = 1;
                    found = 1;
                }
            }
        }
        if (found == 0) {
            printf("no process found deadlock situation");
            printf("\nSystem is NOT in a safe state.\n");
            return 0;
        }
    }

    // Print Safe Sequence
    printf("\nSystem is in a SAFE state.\nSafe sequence is: ");
    for (int i = 0; i < n; i++) {
        printf("P%d ", safeSeq[i]);
    }
    printf("\n");

    return 0;
}

