def hello():
    return "Hello"

print(hello()) # <function func at ...>

greet = hello

del hello

print(greet())