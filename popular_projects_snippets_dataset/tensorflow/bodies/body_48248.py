# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils.py
"""Gets the static batch size of a Layer.

  Args:
    layer: a `Layer` instance.

  Returns:
    The static batch size of a Layer.
  """
batch_input_shape, _ = get_input_shape_and_dtype(layer)
if batch_input_shape is not None:
    exit(tensor_shape.Dimension(batch_input_shape[0]).value)
exit(None)
