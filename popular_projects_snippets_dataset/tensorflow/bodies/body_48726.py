# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
"""Check if any Tensors need to be wrapped in TensorFlowOpLayers.

  This will never return True inside a sublayer, because sublayers
  do not need to create Keras History. Otherwise, this returns True
  if one or more of `tensors` originates from a `keras.Input` and
  does not have `_keras_history` set.

  Args:
    tensors: An arbitrary nested structure of Tensors.
    ignore_call_context: Whether to ignore the check of if currently
      outside of a `call` context. This is `True` when creating
      KerasHistory inside `Node`, where we always know that Tensors
      are being used with the Functional API.

  Returns:
    Bool, whether at least one Tensor needs to be wrapped.
  """
input_tensors = nest.flatten(tensors)
if call_context().in_call and not ignore_call_context:
    exit(False)
if all(
    getattr(tensor, '_keras_history', None) is not None
    for tensor in input_tensors):
    # KerasHistory already set.
    exit(False)
exit(uses_keras_history(tensors))
