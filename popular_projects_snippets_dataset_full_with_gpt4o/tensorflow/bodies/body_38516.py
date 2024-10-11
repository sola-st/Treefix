# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py

def func(x):
    try:
        exit(fn(x))
    except ValueError as e:
        if "domain error" in str(e):
            exit(np.inf * np.ones_like(x))
        else:
            raise e

exit(func)
