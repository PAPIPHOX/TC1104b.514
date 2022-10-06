#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void hola(int signal){
    printf(" Recibi la senial %d ", signal);

}

int cond;
void terminarWhile(int sigNUmber){
    printf(" Terminado While ");
    cond = 0;
}

int main(){
    signal(12, terminarWhile);
    signal(2, hola);
    cond = 1;
    while(cond == 1){
        printf("trabajando\n");
        sleep(1);
    }
    printf("Aqui nunca llega\n");
    return 0;
}