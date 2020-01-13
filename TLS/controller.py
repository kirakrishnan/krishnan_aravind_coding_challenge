def validate_input():
    """
    validates user input. checks if 3 valid values are given as input
    else asks user to re-enter input. 
    :param: input from user
    :return: list of transition values
    """
    try:
        times = input().split(",")
        if(len(times) != 3):
            raise ValueError("please enter 3 valid transition values")
        for k, time in enumerate(times):
            if(not time.isdigit()):
                raise ValueError("Transition values can only be positive integers")
            times[k] = int(time)
        return times
    except ValueError as e:
        print(e)
        times = validate_input()
    except Exception as e:
        print(e)