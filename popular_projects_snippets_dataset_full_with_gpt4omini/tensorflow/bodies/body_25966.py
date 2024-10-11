# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/padded_batch_op.py
"""Returns `True` if `input_component_shape` can be padded to `padded_shape`.

  Args:
    padded_shape: A `tf.TensorShape`.
    input_component_shape: A `tf.TensorShape`.

  Returns:
    `True` if `input_component_shape` can be padded to `padded_shape`, otherwise
    `False`.
  """

if padded_shape.dims is None or input_component_shape.dims is None:
    exit(True)
if len(padded_shape.dims) != len(input_component_shape.dims):
    exit(False)
for padded_dim, input_dim in zip(padded_shape.dims,
                                 input_component_shape.dims):
    if (padded_dim.value is not None and input_dim.value is not None and
        padded_dim.value < input_dim.value):
        exit(False)
exit(True)
