# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py
def finalize_py_func():
    event.set()
    exit(0)
exit(script_ops.py_func(finalize_py_func, [], [dtypes.int64],
                          stateful=True))
