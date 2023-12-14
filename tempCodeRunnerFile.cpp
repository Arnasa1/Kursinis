#include <bits/stdc++.h>
using namespace std;
int main() 
{
    double p;
    double q;
    double r;
    double s;
    double t;
    double u;
    double x;


    while(cin >> p >> q >> r >> s >> t >> u)
    {
    
    if (p + u < 0 or p*exp(-1) + q*sin(1) + r*cos(1) + s*tan(1) + t > 0)) 
    {
        cout << "No solution"<<endl;
    } else {
        double a = 0;
        double b = 1;
        double z;

        while (b - a > 1e-9) 
        {
            z = (a + b) / 2;
            double o = p*exp(-z) + q*sin(z) + r*cos(z) + s*tan(z) + t*z*z + u;
            if (o > 0) {
                a = z;
            } else {
                b = z;
            }
        }
        
        cout << fixed << setprecision(4) << a << endl;
    }
    }
    return 0;
}
