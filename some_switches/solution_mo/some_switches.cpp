#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
using namespace std;

// g++ ./some_switches.cpp -o some_switches.o && ./some_switches.o

// http://www.cplusplus.com/doc/tutorial/files/
// http://www.cplusplus.com/articles/DEN36Up4/
// https://stackoverflow.com/questions/16864067/c-writing-to-file-or-console-by-argument
// http://www.cplusplus.com/reference/string/stoi/
// https://stackoverflow.com/questions/17626619/not-declared-in-this-scope-when-using-strlen

int main(int argc, char* argv[])
{
    int switches_cnt = 100;
    int passes_cnt = 100;
    bool show_hist = false;

    ostream* myOut = &cout;
    ofstream myfile;

    if(argc >= 2) switches_cnt = stoi(argv[1]);
    if(argc >= 3) passes_cnt = stoi(argv[2]);
    if(argc >= 4 && strlen(argv[5]) > 1 ) show_hist=true;
    if(argc >= 5 && strlen(argv[4]) > 1  ){
        myfile.open(argv[4]);
        myOut = &myfile;
    }

    const int const_switches_cnt = switches_cnt;
    bool is_open[const_switches_cnt] = { false };

    for (int pass = 0; pass < passes_cnt; ++pass){
        for (int switch = pass; switch < switches_cnt; switch += pass+1)
            is_open[switch] = !is_open[switch];

        if(show_hist) {
            for (int switch = 0; switch < switches_cnt; ++switch)
                *myOut << (is_open[switch]? "_" : "X") << " ";
            *myOut <<  endl;
        }
    }

    for (int switch = 0; switch < switches_cnt; ++switch)
        *myOut << "Switch " << switch+1 << (is_open[switch]? " is open." : " is closed.") << endl;

    return 0;
}