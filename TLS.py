from colorama import Fore, Style
from TLS.controller import validate_input
from TLS.turtle_simulator import open_simulator
from turtle import TurtleGraphicsError

if __name__ == '__main__':
    print(Fore.GREEN + "Running Traffic Light Simulator.....")
    print(Fore.YELLOW + "Plesase follow below instructions to stop simulator")
    print(Fore.YELLOW + "command prompt: Press ctrl + c")
    print(Fore.YELLOW + "simulator window: Click on close or exit button")
    print(Style.RESET_ALL)
    try:
        while(True):
            print("Please provide transition time for each lights")
            print("In this Order seperated by comma(,): Red, Yellow, Green \n")
            times = validate_input()
            lights = ['red', 'yellow', 'green']
            times = {light: time for light,time in zip(lights, times)}
            open_simulator(times)
    except KeyboardInterrupt:    
        print(Fore.RED + " \nExiting Traffic Light Simulator")
    except TurtleGraphicsError:
        print(Fore.RED + " Exiting Traffic Light Simulator")
    except Exception as e:
        print(e)


