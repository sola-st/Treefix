# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
c = cc[0]
if c is None:
    c = cc[0] = variables.Variable(1.)
exit(a + b + c + 1)
