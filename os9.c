#include <stdio.h>
#include <stdlib.h>

#define MAX_REF 100

int main() {
    int n, frames;
    int ref[MAX_REF];

    printf("Enter number of page references: ");
    if (scanf("%d", &n) != 1 || n <= 0 || n > MAX_REF) {
        printf("Invalid number of references.\n");
        return 1;
    }

    printf("Enter the page reference string (space separated):\n");
    for (int i = 0; i < n; ++i) scanf("%d", &ref[i]);

    printf("Enter number of frames: ");
    if (scanf("%d", &frames) != 1 || frames <= 0) {
        printf("Invalid frame count.\n");
        return 1;
    }

    int *frame = (int*)malloc(frames * sizeof(int));
    int *last_used = (int*)malloc(frames * sizeof(int)); // timestamp of last use
    for (int i = 0; i < frames; ++i) {
        frame[i] = -1;        // -1 indicates empty
        last_used[i] = -1;
    }

    int faults = 0;
    int time = 0; // increment per reference

    for (int i = 0; i < n; ++i) {
        int page = ref[i];
        time++;

        // Check hit
        int hit_index = -1;
        for (int j = 0; j < frames; ++j) {
            if (frame[j] == page) {
                hit_index = j;
                break;
            }
        }

        if (hit_index != -1) {
            // Page hit: update last used time
            last_used[hit_index] = time;
            printf("Ref %d: page %d -> HIT\n", i+1, page);
        } else {
            // Page fault
            faults++;

            // Find an empty frame first
            int empty_index = -1;
            for (int j = 0; j < frames; ++j) {
                if (frame[j] == -1) {
                    empty_index = j;
                    break;
                }
            }

            if (empty_index != -1) {
                frame[empty_index] = page;
                last_used[empty_index] = time;
            } else {
                // Find LRU frame (min last_used)
                int lru_index = 0;
                int min_time = last_used[0];
                for (int j = 1; j < frames; ++j) {
                    if (last_used[j] < min_time) {
                        min_time = last_used[j];
                        lru_index = j;
                    }
                }
                // Replace
                printf("Ref %d: page %d -> FAULT, replace page %d\n", i+1, page, frame[lru_index]);
                frame[lru_index] = page;
                last_used[lru_index] = time;
            }
        }

        // Optional: print current frames
        printf("    Frames: ");
        for (int j = 0; j < frames; ++j) {
            if (frame[j] == -1) printf("- ");
            else printf("%d ", frame[j]);
        }
        printf("\n");
    }

    printf("\nTotal page faults = %d\n", faults);

    free(frame);
    free(last_used);
    return 0;
}

