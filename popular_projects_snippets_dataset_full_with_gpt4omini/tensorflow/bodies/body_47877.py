# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
result = array_ops.reshape(
    inputs, (array_ops.shape(inputs)[0],) + self.target_shape)
if not context.executing_eagerly():
    # Set the static shape for the result since it might lost during array_ops
    # reshape, eg, some `None` dim in the result could be inferred.
    result.set_shape(self.compute_output_shape(inputs.shape))
exit(result)
