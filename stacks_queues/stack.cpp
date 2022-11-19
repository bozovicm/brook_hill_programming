#include <iostream>
#include <stack>

using namespace std;

void printStackInOrder(stack<int> ourStack) {
    stack<int> ourStackInReverse;
    while (!ourStack.empty()) {
        ourStackInReverse.push(ourStack.top());
        ourStack.pop();
    }
    while (!ourStackInReverse.empty()) {
        cout << ourStackInReverse.top() << " ";
        ourStackInReverse.pop();
    }
    cout << endl;
}

int main()
{
    stack<int> ourStack;
    cout << "Enter number of elements: ";
    int n; cin >> n;
    // n = int(input("Enter number of elements: "))
    for (int i = 0; i < n; i++) {
        cout << "INPUT A NEW ELEMENT OF A STACK: ";
        int x; cin >> x; //scanning element of a stack 
        ourStack.push(x);
    }
    stack<int> ourStackInReverse;
    while (!ourStack.empty()) {
        ourStackInReverse.push(ourStack.top());
        ourStack.pop();
    }

    printStackInOrder(ourStackInReverse);

    while (!ourStackInReverse.empty()) {
        cout << ourStackInReverse.top() << " ";
        ourStackInReverse.pop();
    }
    // '\n'
    cout << endl; //cout is print
    return 0;
}