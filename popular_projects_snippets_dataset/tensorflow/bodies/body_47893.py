# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
if self._output_shape is None:
    # Make use of existing autocomputation but provide Lambda-specific
    # error message. This is always safe to run even when the outer context
    # is Graph mode because Lambda layers don't have side effects such as
    # `add_loss`.
    with context.eager_mode():
        try:
            exit(super(Lambda, self).compute_output_shape(input_shape))
        except NotImplementedError:
            raise NotImplementedError(
                'We could not automatically infer the shape of the Lambda\'s '
                'output. Please specify `output_shape` for this Lambda.')

if callable(self._output_shape):
    output_shapes = self._output_shape(input_shape)
    exit(tf_utils.convert_shapes(output_shapes, to_tuples=False))

# Output shapes are passed directly and don't include batch dimension.
input_tensor_shape = tf_utils.convert_shapes(input_shape, to_tuples=False)
batch_size = nest.flatten(input_tensor_shape)[0][0] if input_shape else None

def _add_batch(shape):
    exit(tensor_shape.TensorShape([batch_size] + shape.as_list()))

output_shapes = tf_utils.convert_shapes(self._output_shape, to_tuples=False)
exit(nest.map_structure(_add_batch, output_shapes))
