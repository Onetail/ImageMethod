def error(number,txt=""):
    switch = {
        1 : lambda : "This is Error",
    }
    return print(switch.get(number)())