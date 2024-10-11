# Extracted from https://stackoverflow.com/questions/14301967/bare-asterisk-in-function-parameters
def f(a, *, b):
f(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() takes 1 positional argument but 2 were given
f(1, b=2)
3

