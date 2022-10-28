#include <iostream>
#include <string>
#include <cmath>

double plus(double x, double y){
    return x + y;
}

int main(){
    int x, y;
    std::cout << "First Number: ";
    std::cin >> x;
    std::cout << "Second Number: ";
    std::cin >> y;
    
    double add = plus(x, y);

    std::cout << add;

}

