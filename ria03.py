#include <stdio.h>

int main() {
    int n, i, j;
    int arrival_time[10], burst_time[10], process_id[10];
    int completion_time[10], turnaround_time[10], waiting_time[10];
    int start_time;
    float total_tat = 0, total_wt = 0;

    printf("Enter number of processes: ");
    scanf("%d", &n);

    printf("Enter arrival time for each process:\n");
    for(i = 0; i < n; i++) {
        process_id[i] = i;
        printf("Process %d: ", i);
        scanf("%d", &arrival_time[i]);
    }

    printf("Enter burst time for each process:\n");
    for(i = 0; i < n; i++) {
        printf("Process %d: ", i);
        scanf("%d", &burst_time[i]);
    }

    for(i = 0; i < n - 1; i++) {
        for(j = i + 1; j < n; j++) {
            if(arrival_time[i] > arrival_time[j]) {
                int temp = arrival_time[i];
                arrival_time[i] = arrival_time[j];
                arrival_time[j] = temp;

                temp = burst_time[i];
                burst_time[i] = burst_time[j];
                burst_time[j] = temp;

                temp = process_id[i];
                process_id[i] = process_id[j];
                process_id[j] = temp;
            }
        }
    }

    start_time = 0;
    for(i = 0; i < n; i++) {
        if(start_time < arrival_time[i])
            start_time = arrival_time[i];

        completion_time[i] = start_time + burst_time[i];
        turnaround_time[i] = completion_time[i] - arrival_time[i];
        waiting_time[i] = turnaround_time[i] - burst_time[i];

        total_tat += turnaround_time[i];
        total_wt += waiting_time[i];

        start_time = completion_time[i];
    }

    printf("\nResult Table (Sorted by Arrival Time):\n");
    printf("Process\tAT\tBT\tCT\tTAT\tWT\n");
    for(i = 0; i < n; i++) {
        printf("P%d\t%d\t%d\t%d\t%d\t%d\n",
               process_id[i], arrival_time[i], burst_time[i],
               completion_time[i], turnaround_time[i], waiting_time[i]);
    }

    printf("\nAverage Turnaround Time: %.2f", total_tat / n);
    printf("\nAverage Waiting Time   : %.2f\n", total_wt / n);

    printf("\n---------------------------------------\n");
    printf("Gantt Chart\n\n");

    printf("|");
    for(i = 0; i < n; i++) {
        printf("  P%d  |", process_id[i]);
    }

    printf("\n0");
    for(i = 0; i < n; i++) {
        printf("     %d", completion_time[i]);
    }

    printf("\n");

    return 0;
}
