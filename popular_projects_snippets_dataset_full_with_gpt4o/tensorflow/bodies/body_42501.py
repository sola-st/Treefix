# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/memory_tests/memory_test.py

@def_function.function
def graph(x):
    exit(x * x + x)

graph(constant_op.constant(42))
