#include <iostream>
using namespace std;

int main()
{
    string cuvant, cuvantNou, vocals="aeiou";
    cout << "Cuvantul initial este: ";
    cin >> cuvant;
    for(char& litera : cuvant){
        cuvantNou += litera;
        if(vocals.find(litera) != string::npos )
            cuvantNou += string("p")+litera;
    }
    cout << "Cuvantul nou este: " << cuvantNou << endl;
    return 0;
}


// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

// #include <iostream>
// using namespace std;


// int decToBinary(int n)
// {
// int binaryNum[32];
// int i = 0;
// while (n > 0) {
// binaryNum[i] = n % 2;
// n = n / 2;
// i++;
// }
// int sum = 0;


//  for (int j = i - 1; j >= 0; j--) {
// sum = sum + binaryNum[j];
// }


//  return sum;
// }


// int solution(int X, int Y)
// {
// int Suma = 0;

//  for(int n = X; n <= Y; n++)
// {
// Suma = Suma + decToBinary(n);
// }
// cout << Suma;
// return Suma;
// }
