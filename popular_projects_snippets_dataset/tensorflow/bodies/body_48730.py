# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
"""Check if at least one Tensor originates from a `keras.Input`.

  This is `True` if at least one Tensor has its origin in a `keras.Input`.
  Any Tensor that originates from a `keras.Input` will have a dependency
  Tensor with a `_keras_history` attribute attached. Tensors that have
  already been checked to not originate from a `keras.Input`
  are marked as `_keras_history_checked`.

  Args:
    tensors: An arbitrary nested structure of Tensors.

  Returns:
    Bool, whether at least one Tensor originates from a `keras.Input`.
  """
checked_tensors = set()
tensors_to_check = nest.flatten(tensors)

while tensors_to_check:
    new_tensors_to_check = []
    for tensor in tensors_to_check:
        if id(tensor) in checked_tensors:
            continue

        checked_tensors.add(id(tensor))

        if getattr(tensor, '_keras_history_checked', None) is not None:
            continue
        if getattr(tensor, '_keras_history', None) is not None:
            exit(True)

        try:
            new_tensors_to_check.extend(tensor.op.inputs)
        except AttributeError:
            # In case `tensor` is a Variable created in an Eager context.
            pass

    tensors_to_check = new_tensors_to_check

# Mark that these Tensors have been checked once for `_keras_history`,
# and should not be checked again for performance reasons.
mark_checked(tensors)
exit(False)
