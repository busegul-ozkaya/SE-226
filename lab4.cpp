#include "iostream"
using namespace std;


class Node{
public:
    int data;
    Node* next;
    Node(int d, Node* n){
        data=d;
        next = n;
    }
    Node(){
        data=0;

    }
};
class Stack{
    Node* top;
    int capacity=0;
    int maxSize=3;

public:
    void push(int data) {

        if (capacity < maxSize) {
            Node *temp = new Node();
            temp->data = data;
            temp->next = top;
            top = temp;
            ++capacity;
        } else{
            cout << "capacity is full!"<<endl;
            return;
        }






    }

public:
    void pop(){
        if (top!= nullptr) {
            Node *temp;
            temp = top;
            top = top->next;
            temp->next = nullptr;
            capacity--;


        }else
            cout<<"nothing to pop";

    }
public:
    bool isEmpty() {
        return top== nullptr;
    }

public:
    int Top(){
        return top->data;
    }
public:
    int size(){
        return capacity;
    }

public:
    void display(){
        Node* temp;
        temp=top;
        while (temp!= nullptr){
            cout<<temp->data<<endl;
            temp = temp->next;
        }

    }


};
int main(){
    Stack stack = *new Stack();
    cout<<"Max size is 3"<<endl<<"Pushing numbers:"<<endl;
    stack.push(5);
    stack.push(6);
    cout<<"size is when 6 added: "<<stack.size()<<endl;
    stack.push(7);
    cout<<"size is when 7 added: "<<stack.size()<<endl;
    stack.push(8);
    cout<<"size is when 8 added: "<<stack.size()<<endl;
    stack.display();
    cout<<"top is: "<<stack.Top()<<endl;
    cout<<endl;
    cout<<"is empty?:"<<stack.isEmpty()<<endl;
    cout<<"popping"<<endl;
    stack.pop();
    cout<<"after one pop, top is: "<<stack.Top()<<endl;
    stack.pop();
    stack.pop();
    stack.pop();
    stack.display();
    cout<<endl<<"is empty?:"<<stack.isEmpty()<<endl;
    cout<<"size is:"<<stack.size()<<endl;





}
