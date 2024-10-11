# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
def return_variable():
    exit(resource_variable_ops.ResourceVariable(0.0))

with self.assertRaisesRegex(errors.UnknownError,
                            "Attempting to return a variable"):
    output = script_ops.eager_py_func(
        return_variable, inp=[], Tout=dtypes.float32)
    self.evaluate(output)
