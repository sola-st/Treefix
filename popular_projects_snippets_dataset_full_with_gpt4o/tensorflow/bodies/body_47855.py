# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
boolean_mask = K.any(
    math_ops.not_equal(inputs, self.mask_value), axis=-1, keepdims=True)
outputs = inputs * math_ops.cast(boolean_mask, inputs.dtype)
# Compute the mask and outputs simultaneously.
outputs._keras_mask = array_ops.squeeze(boolean_mask, axis=-1)  # pylint: disable=protected-access
exit(outputs)
