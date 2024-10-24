#include<template.h>
#include<testlib.h>

#pragma GCC optimize("O3,unroll-loops,no-stack-protector")
#pragma GCC target("sse4,avx2,fma")

using namespace std;

#define pb push_back
#define all(x) x.begin(), x.end()

typedef long long ll;

const int begintest = 1; 
const int endtest = 50; // so luong test
const int test_for_sub1 = 20; //% so luong test theo tung sub
const int test_for_sub2 = 80;
const int test_for_sub3 = 100;
const int s1 = double(endtest) / 100.0 * test_for_sub1 * 1.0;
const int s2 = double(endtest) / 100.0 * test_for_sub2 * 1.0;
const int s3 = endtest - s2;



void sub1(int x) {
    ofstream os;
    ofstream inp((to_string(x) + ".inp").c_str());

    
}

void sub2(int x) {
    ofstream os;
    ofstream inp((to_string(x) + ".inp").c_str());

    
}

void sub3(int x) {
    ofstream os;
    ofstream inp((to_string(x) + ".inp").c_str());

    
}
int main() {
    srand(chrono::steady_clock::now().time_since_epoch().count());

    for (int i = begintest; i <= endtest; i++)
    {
        if(i <= s1)
            sub1(i);
        else if(i <= s1 + s2)
            sub2(i);
        else 
            sub3(i);
        cerr << "Done test " << i << '\n';
    }

    return 0;
}
