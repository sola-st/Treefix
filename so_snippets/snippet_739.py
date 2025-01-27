# Extracted from https://stackoverflow.com/questions/2580136/does-python-support-short-circuiting
def fun(i):

fun(1)
executed
1
1 or fun(1)    # due to short-circuiting  "executed" not printed
1
1 and fun(1)   # fun(1) called and "executed" printed 
executed
1
0 and fun(1)   # due to short-circuiting  "executed" not printed 
0

        False    None    0    ""    ()    []     {}

any(fun(i) for i in [1, 2, 3, 4])   # bool(1) = True
executed
True
any(fun(i) for i in [0, 2, 3, 4])   
executed                               # bool(0) = False
executed                               # bool(2) = True
True
any(fun(i) for i in [0, 0, 3, 4])
executed
executed
executed
True

all(fun(i) for i in [0, 0, 3, 4])
executed
False
all(fun(i) for i in [1, 0, 3, 4])
executed
executed
False

5 > 6 > fun(3)    # same as:  5 > 6 and 6 > fun(3)
False                 # 5 > 6 is False so fun() not called and "executed" NOT printed
5 < 6 > fun(3)    # 5 < 6 is True 
executed              # fun(3) called and "executed" printed
True
4 <= 6 > fun(7)   # 4 <= 6 is True  
executed              # fun(3) called and "executed" printed
False
5 < fun(6) < 3    # only prints "executed" once
executed
False
5 < fun(6) and fun(6) < 3 # prints "executed" twice, because the second part executes it again
executed
executed
False

3 and 5    # Second operand evaluated and returned 
5                   
3  and ()
()
() and 5   # Second operand NOT evaluated as first operand () is  false
()             # so first operand returned 

2 or 5    # left most operand bool(2) == True
2    
0 or 5    # bool(0) == False and bool(5) == True
5
0 or ()
()

In [171]: name = raw_input('Enter Name: ') or '<Unknown>'
Enter Name: 

In [172]: name
Out[172]: '<Unknown>'

