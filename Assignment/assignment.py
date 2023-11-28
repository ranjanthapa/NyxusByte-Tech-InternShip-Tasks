def factorial(n):
    result = 1
    for i in range(n, n + 1):
        result *= i
    return result


class CarRacing:
    command = {
        "Start": "Start your Car",
        "Stop": "Stop your car",
        "Exit": "Exit your car"
    }

    def __init__(self):
        self.state = "Stop"

    def aid(self):
        for key, value in CarRacing.command.items():
            print(key, value, sep="-->")

    def play(self):
        exit_game = False
        while not exit_game:
            user_command = input("Enter your command ").lower()
            if user_command == self.state:
                print(f" car is already {self.state}")
            elif user_command == "stop":
                self.state = "stop"
                print("car is stop")
            elif user_command == "start":
                self.state = "start"
                print("car is start")
            elif user_command == "exit":
                confirm_exit = input("Are you sure you want to exit y/n").lower()
                if confirm_exit == "y":
                    exit_game = True

            else:
                print("wrong command")
