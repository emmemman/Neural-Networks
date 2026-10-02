//NIKOLAOS SKRETAS 4493
//EMMANOUILIDIS EMMANOUIL 4669
//KOSTANTINOS DEDIKOUSIS 2962

#include <stdio.h>
#include <stdlib.h>
#include <float.h>
#include <time.h>

#define M 13                 // 3,5,7,9,11,13 
#define RUNS 50             
#define MAX_ITERS 200       // gia asfaleia

typedef struct {
    float x, y;
} Point;

static float sq_dist(Point a, Point b) {
    float dx = a.x - b.x;
    float dy = a.y - b.y;
    return dx*dx + dy*dy;   // eukleidia apostasi 
}

static int read_points(const char *filename, Point **out_pts) {
    FILE *fp = fopen(filename, "r");
    if (!fp) {
        fprintf(stderr, "cant open file: %s\n", filename);
        return -1;
    }

    int cap = 1024;
    int n = 0;
    Point *pts = (Point*)malloc(sizeof(Point) * cap);
    if (!pts) {
        fclose(fp);
        fprintf(stderr, "Out of memory\n");
        return -1;
    }

    float x, y;
    while (fscanf(fp, "%f %f", &x, &y) == 2) {
        if (n >= cap) {
            cap *= 2;
            Point *tmp = (Point*)realloc(pts, sizeof(Point) * cap);
            if (!tmp) {
                free(pts);
                fclose(fp);
                fprintf(stderr, "Out of memory\n");
                return -1;
            }
            pts = tmp;
        }
        pts[n].x = x;
        pts[n].y = y;
        n++;
    }

    fclose(fp);

    if (n <= 0) {
        free(pts);
        fprintf(stderr, "den brethikan simeia sto file.\n");
        return -1;
    }

    *out_pts = pts;
    return n;
}

static void init_centers_random_from_data(const Point *pts, int n, Point *centers) {
    int chosen[M];
    for (int k = 0; k < M; k++) chosen[k] = -1;

    for (int k = 0; k < M; k++) {
        int idx;
        int tries = 0;
        do {
            idx = rand() % n;
            int ok = 1;
            for (int j = 0; j < k; j++) {
                if (chosen[j] == idx) { ok = 0; break; }
            }
            if (ok) break;
            tries++;
        } while (tries < 1000);

        chosen[k] = idx;
        centers[k] = pts[idx];
    }
}

static float kmeans_run(const Point *pts, int n, Point *centers_out) {
    Point centers[M];
    init_centers_random_from_data(pts, n, centers);

    int *assign = (int*)malloc(sizeof(int) * n);
    if (!assign) {
        fprintf(stderr, "Out of memory\n");
        exit(1);
    }
    for (int i = 0; i < n; i++) assign[i] = -1;

    for (int iter = 0; iter < MAX_ITERS; iter++) {
        int changed = 0;

        for (int i = 0; i < n; i++) {
            float bestd = FLT_MAX;
            int bestk = 0;
            for (int k = 0; k < M; k++) {
                float d = sq_dist(pts[i], centers[k]);
                if (d < bestd) {
                    bestd = d;
                    bestk = k;
                }
            }
            if (assign[i] != bestk) {
                assign[i] = bestk;
                changed = 1;
            }
        }

        if (!changed) {
            break;
        }

        float sumx[M], sumy[M];
        int count[M];
        for (int k = 0; k < M; k++) {
            sumx[k] = 0.0f;
            sumy[k] = 0.0f;
            count[k] = 0;
        }

        for (int i = 0; i < n; i++) {
            int k = assign[i];
            sumx[k] += pts[i].x;
            sumy[k] += pts[i].y;
            count[k] += 1;
        }

        for (int k = 0; k < M; k++) {
            if (count[k] > 0) {
                centers[k].x = sumx[k] / count[k];
                centers[k].y = sumy[k] / count[k];
            } else {
                centers[k] = pts[rand() % n];
            }
        }
    }

    // error sum ||xi - mu_k||^2
    float error = 0.0f;
    for (int i = 0; i < n; i++) {
        int k = assign[i];
        error += sq_dist(pts[i], centers[k]);
    }


    for (int k = 0; k < M; k++) centers_out[k] = centers[k];

    free(assign);
    return error;
}

static void save_centers(const char *filename, const Point *centers) {
    FILE *fp = fopen(filename, "w");
    if (!fp) {
        fprintf(stderr, "cant write on file: %s\n", filename);
        return;
    }
    for (int k = 0; k < M; k++) {
        fprintf(fp, "%.6f %.6f\n", centers[k].x, centers[k].y);
    }
    fclose(fp);
}

int main(int argc, char **argv) {
    if (argc < 2) {
        fprintf(stderr, "USE: %s <data_file>\n", argv[0]);
        fprintf(stderr, "to data_file prepei na exei grammes: x1 x2\n");
        return 1;
    }

    srand((unsigned)time(NULL));

    Point *pts = NULL;
    int n = read_points(argv[1], &pts);
    if (n <= 0) return 1;

    float best_error = FLT_MAX;
    Point best_centers[M];

    printf("k-means: M=%d, N=%d, RUNS=%d\n", M, n, RUNS);

    for (int r = 1; r <= RUNS; r++) {
        Point centers[M];
        float err = kmeans_run(pts, n, centers);
        printf("run %2d: error = %.6f\n", r, err);

        if (err < best_error) {
            best_error = err;
            for (int k = 0; k < M; k++) best_centers[k] = centers[k];
        }
    }

    printf("\nBEST: error = %.6f\n", best_error);

    char centers_file[256];
    snprintf(centers_file, sizeof(centers_file), "centers_M%d.txt", M);
    save_centers(centers_file, best_centers);


    char best_file[256];
    snprintf(best_file, sizeof(best_file), "best_M%d.txt", M);
    FILE *fp = fopen(best_file, "w");
    if (fp) {
        fprintf(fp, "M=%d\nbest_error=%.6f\ncenters_file=%s\n", M, best_error, centers_file);
        fclose(fp);
    }

    free(pts);
    return 0;
}
