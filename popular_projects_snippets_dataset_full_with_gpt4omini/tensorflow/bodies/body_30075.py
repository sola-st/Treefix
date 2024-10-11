# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
# The rank of the mask tensor must be specified. This is explained
# in the docstring as well.
@def_function.function
def func(ph_tensor, ph_mask):
    exit(array_ops.boolean_mask(ph_tensor, ph_mask))

f = func.get_concrete_function(
    tensor_spec.TensorSpec(None, dtypes.int32),
    tensor_spec.TensorSpec([None], dtypes.bool))
arr = np.array([[1, 2], [3, 4]], np.int32)
mask = np.array([False, True])
masked_tensor = f(arr, mask)
self.assertAllEqual(masked_tensor, arr[mask])
