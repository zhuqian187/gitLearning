#include <stdio.h>

int x;
int y;
int addTwoNumber() {
    extern int x;
    extern int y;
    x = 1;
    y = 2;
    return x + y;
}

int main() {
    int result;
    result = addTwoNumber();

    printf("result is %d\n", result);
}