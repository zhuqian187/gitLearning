#include <stdio.h>

int main() {
    int sum = 0;
    int i = 0;

    while (i < 101) {
        sum += i;
        i++;
    }

    printf("%d", sum);
}