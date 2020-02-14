#include "XORLL.h"
/*
& - AND
	34&52 -> 32
| - OR
	34|52 -> 54
^ - XOR
	34^52 -> 22
<< - LEFT SHIFT
	see https://en.wikipedia.org/wiki/Bitwise_operations_in_C
	00001101>>1 -> 00000110
	00001101>>3 -> 00000001
>> - RIGHT SHIFT
	same as left, but the other way
~ - NOT
*/
class xorNode{
public:
	xorNode* both;
	int data;

	xorNode(int data, xorNode* previous){

	}
private:

}

class xorList{
public:
	xorNode* head;

	int add(int value);
	int get(int index);

private:
	//
}

int xorList::add(int value){

}

int xorList::get(int index){

}