def error(number,txt=""):
    switch = {
        1 : lambda : "This is Error",
        2 : lambda : "\033[93m[Error] not this path directory . \033[0m"
    }
    return print(switch.get(number)())