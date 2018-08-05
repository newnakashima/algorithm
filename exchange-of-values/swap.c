#include <stdio.h>

void swap(int *x, int *y)
{
    int temp;
    temp = *x; *x = *y; *y = temp;
}

int main()
{
    int a = 2;
    int b = 3;
    printf("Before: a = %d, b = %d\n", a, b);
    swap(&a, &b);
    printf("After: a = %d, b = %d\n", a, b);
}
