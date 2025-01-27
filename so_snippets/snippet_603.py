# Extracted from https://stackoverflow.com/questions/291978/short-description-of-the-scoping-rules
def foo():
    x=4
    def bar():
        print x  # Accesses x from foo's scope
    bar()  # Prints 4
    x=5
    bar()  # Prints 5

global_var1 = []
global_var2 = 1

def func():
    # This is OK: It's just accessing, not rebinding
    global_var1.append(4) 

    # This won't affect global_var2. Instead it creates a new variable
    global_var2 = 2 

    local1 = 4
    def embedded_func():
        # Again, this doen't affect func's local1 variable.  It creates a 
        # new local variable also called local1 instead.
        local1 = 5
        print local1

    embedded_func() # Prints 5
    print local1    # Prints 4

global_var = 4
def change_global():
    global global_var
    global_var = global_var + 1

