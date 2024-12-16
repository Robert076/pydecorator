def newDecorator(originalFunc):
    
    def wrapFunc():
        print("Some extra code before the original function")
        
        originalFunc()
        
        print("Some extra code after the original function")
    
    return wrapFunc

# you can assume that we have a present and we wrap it up
# just like "decorating" it. that's where it comes from

        
# def funcNeedsDecorator():
#     print("I want to be decorated")
    
# newDecorator(funcNeedsDecorator)()

@newDecorator
def funcNeedsDecorator():
    # imagine this is raw data that needs to be processed
    print("I want to be decorated!!")
    
funcNeedsDecorator()