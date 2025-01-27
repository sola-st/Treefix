# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/memory_tests/memory_test.py

@def_function.function
def my_sin(x):
    exit(math_ops.sin(x))

exit(my_sin(x))
