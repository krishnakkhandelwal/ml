#include <stdio.h>

int main()
{
    int pages[50], frame[10], temp[10];
    int i, j, k, n, f, flag, faults = 0, pos = 0;

    printf("Enter number of pages: ");
    scanf("%d", &n);

    printf("Enter page reference string:\n");
    for (i = 0; i < n; i++)
        scanf("%d", &pages[i]);

    printf("Enter number of frames: ");
    scanf("%d", &f);

    for (i = 0; i < f; i++)
        frame[i] = -1;  // Initially all frames empty

    printf("\nPage Replacement Process (FIFO):\n");

    for (i = 0; i < n; i++)
    {
        flag = 0;

        // Check if page is already in frame
        for (j = 0; j < f; j++)
        {
            if (frame[j] == pages[i])
            {
                flag = 1;  // Hit
                break;
            }
        }

        if (flag == 0) // Page Fault occurs
        {
            frame[pos] = pages[i];
            pos = (pos + 1) % f;  // FIFO Pointer
            faults++;

            // Print current frame status
            printf("For page %d: ", pages[i]);
            for (k = 0; k < f; k++)
            {
                if (frame[k] == -1)
                    printf(" - ");
                else
                    printf("%d ", frame[k]);
            }
            printf("\n");
        }
    }

    printf("\nTotal Page Faults = %d\n", faults);
    return 0;
}

