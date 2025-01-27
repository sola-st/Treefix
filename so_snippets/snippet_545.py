# Extracted from https://stackoverflow.com/questions/893333/multiple-variables-in-a-with-statement
with A() as a, B() as b, C() as c:
    doSomething(a,b,c)

with A() as a, B(a) as b, C(a, b) as c:
    doSomething(a, c)

with (
    A() as a, 
    B(a) as b, 
    C(a, b) as c,
):
    doSomething(a, c)

