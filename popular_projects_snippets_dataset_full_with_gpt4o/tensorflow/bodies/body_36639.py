# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py

@def_function.function
def fn():
    exit(x * y * 2.0)

exit(fn())
