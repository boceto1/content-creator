from re import sub

def toCamelCase(string):  
    string = sub(r"(_|-)+", " ", string).title().replace(" ", "")  
    return string[0].lower() + string[1:]  
