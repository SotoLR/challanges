/*
Implement a job scheduler which takes in a function f and an integer n and calls f after n milliseconds
*/

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

void callme(char * txt);
void caller(void (*func_ptr)(char*), char* txt, unsigned long delay);

int main(){
	char * txt = "Hello world";
	void (*func_ptr)(char *);
	func_ptr = callme;
	caller(func_ptr, txt, 10);
	return 0;
}

void caller(void (*func_ptr)(char*), char* txt, unsigned long delay){
	sleep(delay);
	func_ptr (txt);
}

void callme(char * txt){
	printf("%s\n", txt);
}