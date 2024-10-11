# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/function_test.py
# c and d must be known at compile time
x = array_ops.slice(a, c, d)
exit(x)
