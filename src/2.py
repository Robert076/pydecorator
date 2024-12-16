def hello(name = 'Robert'):
    print("The hello() function has been executed!")
    
    def greet():
        return "\t This is the greet() function inside hello!"
    
    def welcome():
        return "\t This welcome() inside hello"
    
    print("I am going to return a function!")
    if name == 'Robert':
        return greet
    else:
        return welcome
    
a = hello('Robert')
print(a())

def cool():
    
    def superCool():
        return 'I am very cool!'
    
    return superCool

someFunc = cool()


print(someFunc())


def test():
    return 'Hi Robert!'

def other(someDefFunc):
    print('Other code runs here!')
    print(someDefFunc())
    
other(test)