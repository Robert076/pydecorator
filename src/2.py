def hello(name = 'Robert'):
    print("The hello() function has been executed!")
    
    def greet():
        return "\t This is the greet() function inside hello!"
    
    def welcome():
        return "\t This welcome() inside hello"
    
    print(greet())
    print(welcome())
    print('This is the end of the hello function')
    
hello()