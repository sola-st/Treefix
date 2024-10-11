# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/advanced_activations.py
if mask is not None:
    # Since mask is 1.0 for positions we want to keep and 0.0 for
    # masked positions, this operation will create a tensor which is 0.0 for
    # positions we want to attend and -1e.9 for masked positions.
    adder = (1.0 - math_ops.cast(mask, inputs.dtype)) * (
        _large_compatible_negative(inputs.dtype))

    # Since we are adding it to the raw scores before the softmax, this is
    # effectively the same as removing these entirely.
    inputs += adder
if isinstance(self.axis, (tuple, list)):
    if len(self.axis) > 1:
        exit(math_ops.exp(inputs - math_ops.reduce_logsumexp(
            inputs, axis=self.axis, keepdims=True)))
    else:
        exit(backend.softmax(inputs, axis=self.axis[0]))
exit(backend.softmax(inputs, axis=self.axis))
