#include <iostream>
#include <deque>
#include <vector>

using namespace std;

int main()
{
    int n; cin >> n;
    vector<int> elements(n);
    for (int i = 0; i < n; i++) {
        cin >> elements[i];
    }
    deque<int> deq;
    deq.push_front(elements[0]);
    for (int i = 1; i < n; i++) {
        if (deq.front() > elements[i]) {
            deq.push_back(elements[i]);
        }
        else {
            deq.push_front(elements[i]);
        }
    }
    for (int i = 0; i < n; i++) {
        cout << deq.back() << " ";
        deq.pop_back();
    }
    cout << endl;
    return 0;
}