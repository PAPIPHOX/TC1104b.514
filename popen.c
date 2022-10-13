#include <stdio.h>

int main(){
    FILE *lsOutput;
    FILE *tomayaIpunt;
    char readBuffer[80];
    lsOutput = popen("ls *c", "r");
    tomayaIpunt = popen("wc -l", "w");

    while(fgets(readBuffer, 80, lsOutput)){
        fputs(readBuffer, tomayaIpunt);
    }

    pclose(lsOutput);
    pclose(tomayaIpunt);
}