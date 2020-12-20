#include <stdio.h>
int main(void) {
float a;
float b;
float temp;
printf("test for 40 fibonacci's first numbers\n");
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
printf("Total: \n");
printf("%.2f\n", (float)(a));
return 0;
}
