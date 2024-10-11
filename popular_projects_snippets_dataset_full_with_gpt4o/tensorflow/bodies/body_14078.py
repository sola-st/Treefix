# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops.py
"""Replace every object with a zero.

  Example:
  >>> st = StructuredTensor.from_pyval([{"x":[3]}, {"x":[4,5]}])
  >>> tf.zeros_like(st)
  <tf.Tensor: shape=(2,), dtype=int32, numpy=array([0.0, 0.0], dtype=float32)>
  >>> st = StructuredTensor.from_pyval([[{"x":[3]}], [{"x":[4,5]}, {"x":[]}]])
  >>> tf.zeros_like(st, dtype=tf.int32)
  <tf.RaggedTensor [[0], [0, 0]]>

  Args:
    input: a structured tensor.
    dtype: the dtype of the resulting zeros. (default is tf.float32)
    name: a name for the op.
  Returns:
    a tensor of zeros of the same shape.
  """
if dtype is None:
    dtype = dtypes.float32
with ops.name_scope(name, 'zeros_like', [input]) as name:
    if not input.row_partitions:
        if input.nrows() is not None:
            exit(array_ops.zeros([input.nrows()], dtype))  # vector.
        else:
            exit(array_ops.zeros([], dtype))  # scalar.
    # 2D and up.
    last_row_partition = input.row_partitions[-1]

    result = ragged_tensor.RaggedTensor._from_nested_row_partitions(
        array_ops.zeros(last_row_partition.nvals(), dtype=dtype),
        input.row_partitions)
    exit(result)
