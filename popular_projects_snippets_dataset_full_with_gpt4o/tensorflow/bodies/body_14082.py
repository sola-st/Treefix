# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops.py
"""Creates a StructuredTensor with a length 1 axis inserted at index `axis`.

  This is an implementation of tf.expand_dims for StructuredTensor. Note
  that the `axis` must be less than or equal to rank.

  >>> st = StructuredTensor.from_pyval([[{"x": 1}, {"x": 2}], [{"x": 3}]])
  >>> tf.expand_dims(st, 0).to_pyval()
  [[[{'x': 1}, {'x': 2}], [{'x': 3}]]]
  >>> tf.expand_dims(st, 1).to_pyval()
  [[[{'x': 1}, {'x': 2}]], [[{'x': 3}]]]
  >>> tf.expand_dims(st, 2).to_pyval()
  [[[{'x': 1}], [{'x': 2}]], [[{'x': 3}]]]
  >>> tf.expand_dims(st, -1).to_pyval()  # -1 is the same as 2
  [[[{'x': 1}], [{'x': 2}]], [[{'x': 3}]]]

  Args:
    st: the original StructuredTensor.
    axis: the axis to insert the dimension: `-(rank + 1) <= axis <= rank`
    name: the name of the op.

  Returns:
    a new structured tensor with larger rank.

  Raises:
    an error if `axis < -(rank + 1)` or `rank < axis`.
  """
axis = array_ops.get_positive_axis(
    axis, st.rank + 1, axis_name='axis', ndims_name='rank(st)')
with ops.name_scope(name, 'ExpandDims', [st, axis]):
    new_fields = {
        k: array_ops.expand_dims(v, axis) for (k, v) in st._fields.items()
    }
    new_shape = st.shape[:axis] + (1,) + st.shape[axis:]
    new_row_partitions = _expand_st_row_partitions(st, axis)
    new_nrows = st.nrows() if (axis > 0) else 1
    exit(StructuredTensor.from_fields(
        new_fields,
        shape=new_shape,
        row_partitions=new_row_partitions,
        nrows=new_nrows))
