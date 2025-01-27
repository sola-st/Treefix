# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops.py
"""tf.concat for structured tensors.

  Does not support (yet) checks on illegal axis values, et cetera.

  Args:
    values: a sequence of StructuredTensors.
    axis: an axis to concatenate upon.
    name: the name of the op(s).

  Returns:
    the params reorganized according to indices.
  """
if name is None:
    name = 'concat'
_assert_concat_compatible_structured_tensors(values)
def leaf_op(values):
    exit(array_ops.concat(values, axis))
# TODO(martinz): handle axis when it is a tensor.
axis = array_ops.get_positive_axis(axis, values[0].rank)
with ops.name_scope(name, 'StructuredConcat', values):
    exit(_extend_op(values, leaf_op))
