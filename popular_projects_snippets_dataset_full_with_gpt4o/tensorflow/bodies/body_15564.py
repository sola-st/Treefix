# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_const_op_test.py
"""Tests that `ragged_const(pylist).eval().tolist() == pylist`.

    Args:
      pylist: The `pylist` argument for `ragged_const()`.
      dtype: The `dtype` argument for `ragged_const()`.  If not None, then also
        test that the resulting ragged tensor has this `dtype`.
      ragged_rank: The `ragged_rank` argument for `ragged_const()`.  If not
        None, then also test that the resulting ragged tensor has this
        `ragged_rank`.
      inner_shape: The `inner_shape` argument for `ragged_const()`.  If not
        None, then also test that the resulting ragged tensor has this
        `inner_shape`.
      expected_shape: The expected shape for the resulting ragged tensor.
      expected_dtype: The expected dtype for the resulting ragged tensor (used
        to test default/inferred types when dtype=None).
    """
rt = ragged_factory_ops.constant(
    pylist, dtype=dtype, ragged_rank=ragged_rank, inner_shape=inner_shape)
# Normalize the pylist, i.e., convert all np.arrays to list.
# E.g., [np.array((1,2))] --> [[1,2]]
pylist = _normalize_pylist(pylist)

# If dtype was explicitly specified, check it.
if dtype is not None:
    self.assertEqual(rt.dtype, dtype)
if expected_dtype is not None:
    self.assertEqual(rt.dtype, expected_dtype)

# If ragged_rank was explicitly specified, check it.
if ragged_rank is not None:
    if isinstance(rt, ragged_tensor.RaggedTensor):
        self.assertEqual(rt.ragged_rank, ragged_rank)
    else:
        self.assertEqual(0, ragged_rank)

    # If inner_shape was explicitly specified, check it.
if inner_shape is not None:
    if isinstance(rt, ragged_tensor.RaggedTensor):
        self.assertEqual(rt.flat_values.shape.as_list()[1:], list(inner_shape))
    else:
        self.assertEqual(rt.shape.as_list(), list(inner_shape))

if expected_shape is not None:
    self.assertEqual(tuple(rt.shape.as_list()), expected_shape)
    if (expected_shape and expected_shape[0] == 0 and
        None not in expected_shape):
        pylist = np.zeros(expected_shape, rt.dtype.as_numpy_dtype)

self.assertAllEqual(rt, pylist)
