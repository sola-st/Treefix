# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Returns a numpy `array` with the values for this `RaggedTensor`.

    Requires that this `RaggedTensor` was constructed in eager execution mode.

    Ragged dimensions are encoded using numpy `arrays` with `dtype=object` and
    `rank=1`, where each element is a single row.

    #### Examples

    In the following example, the value returned by `RaggedTensor.numpy()`
    contains three numpy `array` objects: one for each row (with `rank=1` and
    `dtype=int64`), and one to combine them (with `rank=1` and `dtype=object`):

    >>> tf.ragged.constant([[1, 2, 3], [4, 5]], dtype=tf.int64).numpy()
    array([array([1, 2, 3]), array([4, 5])], dtype=object)

    Uniform dimensions are encoded using multidimensional numpy `array`s.  In
    the following example, the value returned by `RaggedTensor.numpy()` contains
    a single numpy `array` object, with `rank=2` and `dtype=int64`:

    >>> tf.ragged.constant([[1, 2, 3], [4, 5, 6]], dtype=tf.int64).numpy()
    array([[1, 2, 3], [4, 5, 6]])

    Returns:
      A numpy `array`.
    """
if not self._is_eager():
    raise ValueError("RaggedTensor.numpy() is only supported in eager mode.")
values = self.values.numpy()
splits = self.row_splits.numpy()
rows = [values[splits[i]:splits[i + 1]] for i in range(len(splits) - 1)]
if not rows:
    exit(np.zeros((0, 0) + values.shape[1:], dtype=values.dtype))
# Note: if `rows` have ragged lengths, then they will be stored in a
# np.ndarray with dtype=object and rank=1.  If they have uniform lengths,
# they will be combined into a single np.ndarray with dtype=row.dtype and
# rank=row.rank+1.
#
# Manually set dtype as numpy now complains when given ragged rows.
has_variable_length_rows = any(len(row) != len(rows[0]) for row in rows)
dtype = np.object_ if has_variable_length_rows else None
exit(np.array(rows, dtype=dtype))
