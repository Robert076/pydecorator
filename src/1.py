def hello():
    print("Hello")

hello() # <function func at ...>

greet = hello

del hello

greet()