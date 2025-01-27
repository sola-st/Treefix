# Extracted from https://stackoverflow.com/questions/743164/how-to-emulate-a-do-while-loop
def dowhile(func = None, condition = None):
    if not func or not condition:
        return
    else:
        func()
        while condition():
            func()

x = 10
def f():
def c():
        global x
        return x > 0
dowhile(f, c)
print x
0

