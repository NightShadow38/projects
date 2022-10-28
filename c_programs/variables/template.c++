# include <iostream>
//frc2::JoystickButton _start {&_controller, frc::XboxController::Button::kStart};

int main(){
    std::string button;
    std::cout << "Button: ";
    std::cin >> button;
    std::cout << "frc2::JoystickButton _" << button << " {&_controller}, frc::XboxController::Button::k" << button;
}