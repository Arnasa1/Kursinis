#include <bits/stdc++.h>
using namespace std;
int main()
{
    int a[3];

    int n = 3;

    for(int i=0;i<n;i++)
    {
        cin >> a[i];

    }

   
    cout <<*max_element(a , a + n) << endl;
}