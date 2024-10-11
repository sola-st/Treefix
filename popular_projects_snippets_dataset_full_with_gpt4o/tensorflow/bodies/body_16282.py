# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_constant_value_op_test.py
"""Tests that `ragged_value(pylist).to_list() == pylist`."""
rt = ragged_factory_ops.constant_value(
    pylist, dtype=dtype, ragged_rank=ragged_rank, inner_shape=inner_shape)
# Normalize the pylist, i.e., convert all np.arrays to list.
# E.g., [np.array((1,2))] --> [[1,2]]
pylist = _normalize_pylist(pylist)
# If dtype was explicitly specified, check it.
if expected_dtype is not None:
    self.assertEqual(rt.dtype, expected_dtype)
elif dtype is not None:
    self.assertEqual(rt.dtype, dtype)

# If ragged_rank was explicitly specified, check it.
if ragged_rank is not None:
    if isinstance(rt, ragged_tensor_value.RaggedTensorValue):
        self.assertEqual(rt.ragged_rank, ragged_rank)
    else:
        self.assertEqual(0, ragged_rank)

    # If inner_shape was explicitly specified, check it.
if inner_shape is not None:
    if isinstance(rt, ragged_tensor_value.RaggedTensorValue):
        self.assertEqual(rt.flat_values.shape[1:], inner_shape)
    else:
        self.assertEqual(rt.shape, inner_shape)

if expected_shape is not None:
    self.assertEqual(tuple(rt.shape), expected_shape)

if rt.shape:
    if isinstance(rt, ragged_tensor_value.RaggedTensorValue):
        self.assertEqual(rt.to_list(), pylist)
    else:
        self.assertEqual(rt.tolist(), pylist)
    if expected_shape is not None:
        self.assertEqual(rt.shape, expected_shape)
else:
    self.assertEqual(rt, pylist)
    if expected_shape is not None:
        self.assertEqual((), expected_shape)
