#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
char stack[20];
int top = -1;
int flag=0;
char string1[20];
void push(char s)
{
top++;
stack[top]=s;
}
char pop()
{
char x;
x = stack[top];
top--;
return x;
}
int isStackEmpty()
{
if(top == -1)
return 1;
else
return 0;
}
void accept()
{
cout<<"Enter the string: "<<endl;
cin>>string1;
cout<<"Entered String is "<<string1<<endl;
}
void checkparenthesis()
{
flag = 0;
for(int i=0;string1[i]!='\0';i++)
{
if(string1[i] == '(' || string1[i] == '{' || string1[i] == '[')
{
push(string1[i]);
}
else if(string1[i] == ')')
{
if(pop() != '(')
flag = 1;
}
else if(string1[i] == '}')
{
if(pop() != '{')
flag = 1;
}
else if(string1[i] == ']')
{
if(pop() != '[')
flag = 1;
}
}
if(isStackEmpty() && flag == 0)
cout<<"Paranthesis are balanced";
else
cout<<"Paranthesis are not balanced";
}
void display()
{
int i;
cout<<"\n"<<"Contents of Stack:\n"<<string1;
for(i = 0; i <= top ; i++)
cout<<"\n"<<stack[i]<<endl;
}
int main()
{
int ch;
do
{
cout<<"\n***** MENU *****"<<endl;
cout<<"1. Enter String."<<endl;
cout<<"2. Display String."<<endl;
cout<<"3. Check Parenthesis is present in string or not."<<endl;
cout<<"Enter Choice:"<<endl;
cin>>ch;
switch(ch)
{
case 1: accept();
break;
case 2: display();
break;
case 3: checkparenthesis();
break;
}
}while(ch<4);

}
