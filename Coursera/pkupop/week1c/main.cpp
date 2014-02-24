#include <stdio.h>
#include <stdlib.h>     //qsort?
#include <iostream>

using namespace std;

//lecture 1: function pointer

int MyCompare(const void * elem1, const void * elem2) {
    unsigned int *p1, *p2;
    p1 = (unsigned int *) elem1;
    p2 = (unsigned int *) elem2;
    return (*p1 % 10) - (*p2 % 10);
}

#define NUM 5
int main(int argc, char *argv[])    // argc >= 1
{
    //1-1
    unsigned int an[NUM] = {8, 123, 11, 10, 4};
    qsort(an, NUM, sizeof(unsigned int), MyCompare); //!!
    for (int i = 0; i < NUM; i++)
        printf("%d ", an[i]);
    //1-2
    for (int i = 0; i< argc; i++)
        printf("%s\n", argv[i]);
    //1-homework
    printf("Home work result:\n");
    printf("No.1: %d\n", 34 & 27);
    printf("No.2: %x\n", -12 >> 2);
    printf("No.3: %d\n", 26 | 14);
    printf("No.4: %d\n", 18 ^ 22);
    printf("No.5: ");
    int *p = new int[12];
    cout << sizeof(*p) << endl;
    printf("No.6: ");
    int a = 3, b = 5;
    int &r = a;
    r = b;
    b = 7;
    printf("%d\n", r);

    printf("Hello World!\n");
    return 0;
}

