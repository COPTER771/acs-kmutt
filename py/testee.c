#include <stdio.h>

int main() {
    int R, C;
    scanf("%d %d", &R, &C);

    int A[10][10];
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &A[i][j]);
        }
    }


    for (int j = 0; j < C; j++) {  
        for (int i = 0; i < R; i++) {
            printf("%d", A[i][j]);
            if (i < R - 1) printf(" ");
        }
        printf("\n");
    }

    return 0;
}
