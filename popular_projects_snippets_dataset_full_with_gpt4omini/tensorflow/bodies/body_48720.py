# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
"""Retrieves the output mask(s) of the previous node.

  Args:
      input_tensors: An arbitrary structure of Tensors.

  Returns:
      A mask tensor or list of mask tensors.
  """

def _collect_previous_mask(x):
    exit(getattr(x, '_keras_mask', None))

exit(nest.map_structure(_collect_previous_mask, input_tensors))
