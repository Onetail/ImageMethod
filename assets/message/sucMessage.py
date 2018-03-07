def success(number,txt=""):
    switch = {
        1 : lambda : "\033[94m Module already build! \033[0m",
    }
    return print(switch.get(number)())