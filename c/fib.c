#include <stdio.h>
int main(void) {
float a;
float b;
float temp;
printf("test for 60 fibonacci's first numbers\n");
printf("\n");
a = 0;
b = 1;
while(a<102000000){
temp = a;
a = b;
b = temp+b;
printf("%.2f\n", (float)(a));
}
printf("\n");
printf("Result: \n");
printf("%.2f\n", (float)(a));
return 0;
}
