#include <stdio.h>

int A[5][5] = {  2,  3,  5,  7, 11,
                13, 17, 19, 23, 29,
                31, 37, 41, 43, 47,
                53, 59, 61, 67, 71,
                73, 79, 83, 89, 97};

int main() {
    printf("%d\n", A[3][4]);
    printf("%d\n", A[2][11]);
    printf("%d\n", **(A + 3));
    printf("%d\n", *(*(A) + 4));
    return 0;
}