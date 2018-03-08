def message(number,txt=""):
    switch = {
        1 : lambda : "Call  message\033[0m",
        2 : lambda : "\033[2m {:10} \033[0m".format(txt),
        3 : lambda : "\033[34m {:10} \033[0m".format(txt),
    }
    
    return print(switch.get(number)())