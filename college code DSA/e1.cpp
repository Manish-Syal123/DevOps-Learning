#include <iostream>
#include <string.h>
#include<stdio.h>
#include<stdlib.h>
#include<string>
using namespace std;
class Queue
{
 public:
 const static int size =10;
 int front=-1,rear=-1;
 int array[size];
 
 void push(int x)
 {
 if(rear==size-1)
 {
cout<<"Queue overflow!!";
 
 }
 array[++rear]=x;
 }
 int pop()
 {
 if(front==rear)
 {
 cout<<"queue underflow!!";
 
 }
 return array[++front];
 }
void display()
{
 if(front==rear)
 {
 cout<<"Queue is empty";
 }
 //cout<<"\nQueue contains ";
 cout<<"\n Jobs in queue are...:\n";
 for(int i=front+1;i<=rear;i++)
 {
 cout<<array[i]<<" ";
 }
}
};
 int main()
 {
 Queue q;
 int ch,job;
do
{
cout<<"\n ********MENU*********";
cout<<"\n 1)Insert job id";
cout<<"\n 2)Delete job id";
cout<<"\n 3)Display job id";
cout<<"\n 4)Exit";
cout<<"\n Enter your choice....:";
cin>>ch;
switch(ch)
{
case 1: cout<<"\n Enter Job id...:";
cin>>job;
q.push(job);
break;
case 2: job = q.pop();
cout<<"\nDeleted job is...:"<<job;
break;
case 3: q.display();
break;
}
}while(ch<4);
 }
