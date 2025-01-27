# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
"""Marks that these Tensors should not be tracked.

  This prevents Layers from attempting to create TensorFlowOpLayers
  for these Tensors.

  Args:
    tensors: An arbitrary structure of Tensors.
  """

def _mark_checked(tensor):
    tensor._keras_history_checked = True  # pylint: disable=protected-access

nest.map_structure(_mark_checked, tensors)
