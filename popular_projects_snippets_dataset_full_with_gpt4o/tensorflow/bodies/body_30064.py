# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
"""Check equivalence between boolean_mask and numpy masking."""
if make_mask is None:
    make_mask = lambda shape: self.rng.randint(0, 2, size=shape).astype(bool)
arr = np.random.rand(*arr_shape)
mask = make_mask(arr_shape[:ndims_mask])
if axis is not None:
    mask = make_mask(arr_shape[axis:ndims_mask + axis])
if axis is None or axis == 0:
    masked_arr = arr[mask]
elif axis == 1:
    masked_arr = arr[:, mask]
elif axis == 2:
    masked_arr = arr[:, :, mask]
masked_tensor = array_ops.boolean_mask(arr, mask, axis=axis)

# Leading dimension size of masked_tensor is always unknown until runtime
# since we don't how many elements will be kept.
leading = 1 if axis is None else axis + 1
self.assertAllEqual(masked_tensor.get_shape()[leading:],
                    masked_arr.shape[leading:])

self.assertAllClose(masked_arr, masked_tensor)
