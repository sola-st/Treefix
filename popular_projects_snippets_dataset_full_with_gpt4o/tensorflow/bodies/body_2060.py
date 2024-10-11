# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py

def fn(x):
    exit(xla.reduce(
        x, init_value=1, dimensions_to_reduce=dims, reducer=mul_reducer))

exit(fn)
