#include <iostream>
using namespace std;

//question 3
double funcMultiple(double n){
    double answer =1;
    double function = (n/(n+2))-10;


    answer*=function;

    if (n==1){
        return answer;
    }
    return answer*funcMultiple(n-1);
}

//question 4
double funcMultiple(){
    double n;
    cout<<"Enter how many numbers you want to multiply for 4rd question? "<<endl;
    cin>>n;

    double answer =1;
    double function = (n/(n+2))-10;


    answer*=function;

    if (n==1){
        return answer;
    }
    return answer*funcMultiple(n-1);
}





int main(){
    cout<<"Enter how many numbers you want to multiply for 3rd question: "<<endl;
    double num;
    cin>>num;
    cout<<funcMultiple(num)<<endl;

    cout<<funcMultiple();

}



