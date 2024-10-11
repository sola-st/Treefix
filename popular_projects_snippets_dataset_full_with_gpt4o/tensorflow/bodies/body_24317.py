# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
output = math_ops.sin(x)
@def_function.function
def grad(dy):
    # `dy` will come in as 1.0. Taking log of -1.0 leads to NaN.
    exit(math_ops.log(-dy))
exit((output, grad))
