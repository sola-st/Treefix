# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
if array_ops.constant(False):
    exit(array_ops.constant(1))
else:
    exit(script_ops.eager_py_func(
        func=lambda: array_ops.constant([2.]), inp=(), Tout=dtypes.int32))
