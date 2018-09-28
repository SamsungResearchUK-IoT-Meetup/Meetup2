#include "mbed.h"
 
DigitalOut red  (p5);
DigitalOut green(p6);
DigitalOut blue (p7);
 
int main() {
    red = 1;
    green = blue = 0;
    wait(0.2);
    
    green = 1;
    red = blue = 0;
    wait(0.2);
 
    blue = 1;
    red = green = 0;
    wait(0.2);
}
