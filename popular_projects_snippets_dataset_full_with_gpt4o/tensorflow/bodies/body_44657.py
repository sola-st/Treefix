# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/data_structures_test.py
l = list_ops.empty_tensor_list(
    element_shape=None, element_dtype=dtypes.variant)

opts = data_structures.ListStackOpts(
    element_dtype=dtypes.int32, original_call=None)

# TODO(mdan): Allow stacking empty lists if the dtype and shape are known.
with self.assertRaises(ValueError):
    data_structures.list_stack(l, opts)
