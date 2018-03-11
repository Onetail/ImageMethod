def error(number,txt=""):
    switch = {
        1 : lambda : "This is Error",
        2 : lambda : "\033[93m[Error] not have this path directory . \033[0m",
        3 : lambda : "\033[93m[Error] not have this type . \033[0m"
    }
    return print(switch.get(number)())