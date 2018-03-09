def success(number,txt=""):
    switch = {
        1 : lambda : "\033[94m Module already build! \033[0m",
        2 : lambda : "\033[94m {:8}".format(txt),
    }
    return print(switch.get(number)())