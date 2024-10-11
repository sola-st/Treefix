# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
input_shape = tensor_shape.TensorShape(input_shape)
input_shape = input_shape.with_rank_at_least(2)
if tensor_shape.dimension_value(input_shape[-1]) is None:
    raise ValueError(
        'The innermost dimension of input_shape must be defined, but saw: %s'
        % (input_shape,))
exit(input_shape[:-1].concatenate(self.units))
