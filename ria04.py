#include <stdio.h>

int main() {
    int n, i;
    int arrival_time[10], burst_time[10], process_id[10], remain[10];
    int completion_time[10], turnaround_time[10], waiting_time[10];
    int gantt_process[100], gantt_time[100];
    float total_tat = 0, total_wt = 0;

    // Input
    printf("Enter number of processes: ");
    scanf("%d", &n);

    printf("Enter arrival time for each process:\n");
    for (i = 0; i < n; i++) {
        process_id[i] = i + 1;
        printf("P%d: ", i + 1);
        scanf("%d", &arrival_time[i]);
    }

    printf("Enter burst time for each process:\n");
    for (i = 0; i < n; i++) {
        printf("P%d: ", i + 1);
        scanf("%d", &burst_time[i]);
        remain[i] = burst_time[i];
    }

    // SRTF scheduling simulation
    int time = 0, completed = 0, gc = 0;
    while (completed < n) {
        int idx = -1, min = 1e9;
        for (i = 0; i < n; i++) {
            if (arrival_time[i] <= time && remain[i] > 0 && remain[i] < min) {
                min = remain[i];
                idx = i;
            }
        }

        if (idx != -1) {
            if (gc == 0 || gantt_process[gc - 1] != process_id[idx]) {
                gantt_process[gc] = process_id[idx];
                gantt_time[gc] = time;
                gc++;
            }
            remain[idx]--;
            if (remain[idx] == 0) {
                completed++;
                completion_time[idx] = time + 1;
                turnaround_time[idx] = completion_time[idx] - arrival_time[idx];
                waiting_time[idx] = turnaround_time[idx] - burst_time[idx];
                total_tat += turnaround_time[idx];
                total_wt += waiting_time[idx];
            }
        }
        time++;
    }
    gantt_time[gc] = time;

    // Output Table (sorted by process ID)
    printf("\nProcess\tAT\tBT\tCT\tTAT\tWT\n");
    for (i = 0; i < n; i++) {
        int id = i + 1;
        int idx;
        for (idx = 0; idx < n; idx++) {
            if (process_id[idx] == id) break;
        }
        printf("P%d\t%d\t%d\t%d\t%d\t%d\n",
               process_id[idx], arrival_time[idx], burst_time[idx],
               completion_time[idx], turnaround_time[idx], waiting_time[idx]);
    }

    printf("\nAverage Turnaround Time: %.2f", total_tat / n);
    printf("\nAverage Waiting Time   : %.2f\n", total_wt / n);

    // Gantt Chart
    printf("\nGantt Chart:\n\n");
    for (i = 0; i < gc; i++) {
        printf("|  P%d  ", gantt_process[i]);
    }
    printf("|\n");

    printf("%d", gantt_time[0]);
    for (i = 1; i <= gc; i++) {
        printf("     %d", gantt_time[i]);
    }
    printf("\n");

    return 0;
}
