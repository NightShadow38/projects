#include <iostream>
#include <string>
#include <cmath>

double plus(double x, double y){return x + y;}
double minus(double x, double y){return x - y;}
double multi(double x, double y){return x * y;}
double divide(double x, double y){return x / y;}

int main(){

    int x, y;
    std::string symbol;
    std::cout << "Symbols: +, -, *, / \n";
    std::cout << "First Number: ";
    std::cin >> x;
    std::cout << "Symbol: ";
    std::cin >> symbol;
    std::cout << "Second Number: ";
    std::cin >> y;

    double add = plus(x, y);
    double sub = minus(x, y);
    double mul = multi(x, y);
    double div = divide(x, y);
    
    if(symbol == "+"){std::cout << add;}
    else if(symbol == "-"){std::cout << sub;}
    else if(symbol == "*"){std::cout << mul;}
    else if(symbol == "/"){std::cout << div;}
    else {std::cout << "error";}

}

