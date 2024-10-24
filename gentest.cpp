#include "testlib.h"

using namespace std;

void writeTest(int test) {
    startTest(test);

    int a = rnd.next(1, test * test);
    int b = rnd.next(1, test * test);
    println(a, b);
}

int main(int argc, char *argv[]) {
    registerGen(argc, argv, 1);

    for (int i = 1; i <= 10; i++)
        writeTest(i);
}