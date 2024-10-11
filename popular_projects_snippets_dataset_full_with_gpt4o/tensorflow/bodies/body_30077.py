# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
# The rank of the mask tensor must be specified. This is explained
# in the docstring as well.
@def_function.function
def func(tensor, mask):
    exit(array_ops.boolean_mask(tensor, mask))

with self.assertRaisesRegex(ValueError, "dimensions must be specified"):
    _ = func.get_concrete_function(
        tensor_spec.TensorSpec([None, 2], dtypes.int32),
        tensor_spec.TensorSpec(None, dtypes.bool))
