# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def test_fn():
    if array_ops.constant(False):
        exit(array_ops.constant(1))
    else:
        exit(script_ops.eager_py_func(
            func=lambda: array_ops.constant([2.]), inp=(), Tout=dtypes.int32))

error_pattern = re.compile(r'Graph execution error.*func=lambda', re.DOTALL)
with self.assertRaisesRegex(errors.InvalidArgumentError, error_pattern):
    test_fn()
