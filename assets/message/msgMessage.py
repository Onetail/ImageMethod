def message(number,txt=""):
    switch = {
        1 : lambda : "Call  message\033[0m",
    }
    
    return print(switch.get(number)())