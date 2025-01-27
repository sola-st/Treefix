# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
@polymorphic_function.function
def func(x):
    exit(2 * x)

func_a = func.get_concrete_function(
    tensor_spec.TensorSpec([None], dtypes.int32))
func_b = func.get_concrete_function(
    tensor_spec.TensorSpec([None], dtypes.int32))

self.assertIs(func_a, func_b)
