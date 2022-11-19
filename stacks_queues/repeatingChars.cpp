/*
We are given an input string. Print that string so that
we delete all series of repeating charachters

baaaba
bba
a

brookhill
brookhi
brkhi

broorhill
broorhi
brrhi
bhi
*/
#include <iostream>
#include <stack>

using namespace std;

int main()
{   
    cout << "Enter the beginning string: " ;
    string s; cin >> s;
    int length = s.length(); // holds value of number of letters in our string
    
    stack<char> stacky;

    for (int i = 0; i < length; i++) {
        
        if (stacky.empty()) {
            stacky.push(s[i]);
            continue;
        } // O(1)

        if (stacky.top() != s[i]) {
            stacky.push(s[i]);
        }
        else {
            int j = 0;
            while (s[i] == s[i + j]) {
                j++;
            }
            i = i + j - 1;
            stacky.pop();
        }
    }
    stack<char> stackyPrint;
    
    while (!stacky.empty()) {
        stackyPrint.push(stacky.top());
        stacky.pop();
    }

    while (!stackyPrint.empty()) {
        cout << stackyPrint.top();
        stackyPrint.pop();
    }
    cout << '\n';
    return 0;
}