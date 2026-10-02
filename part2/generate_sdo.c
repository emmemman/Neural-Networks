#include <stdio.h>
#include <stdlib.h>
#include <time.h>

float rnd(float a, float b) {
    return a + (b - a) * ((float)rand() / RAND_MAX);
}

void gen(FILE *fp, int n, float x1, float x2, float y1, float y2) {
    for (int i = 0; i < n; i++) {
        float x = rnd(x1, x2);
        float y = rnd(y1, y2);
        fprintf(fp, "%.6f %.6f\n", x, y);
    }
}

int main() {
    srand((unsigned)time(NULL));

    FILE *fp = fopen("sdo_data.txt", "w");
    if (!fp) {
        printf("Cannot create file\n");
        return 1;
    }

    gen(fp, 150, 0.75, 1.25, 0.75, 1.25);
    gen(fp, 150, 0.0, 0.5, 0.0, 0.5);
    gen(fp, 150, 0.0, 0.5, 1.5, 2.0);
    gen(fp, 150, 1.5, 2.0, 0.0, 0.5);
    gen(fp, 150, 1.5, 2.0, 1.5, 2.0);

    gen(fp, 75, 0.6, 0.8, 0.0, 0.4);
    gen(fp, 75, 0.6, 0.8, 1.6, 2.0);
    gen(fp, 75, 1.2, 1.4, 0.0, 0.4);
    gen(fp, 75, 1.2, 1.4, 1.6, 2.0);

    gen(fp, 150, 0.0, 2.0, 0.0, 2.0); 

    fclose(fp);
    return 0;
}