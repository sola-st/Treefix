# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/pooling.py
steps_axis = 1 if self.data_format == 'channels_last' else 2
if mask is not None:
    mask = math_ops.cast(mask, inputs[0].dtype)
    mask = array_ops.expand_dims(
        mask, 2 if self.data_format == 'channels_last' else 1)
    inputs *= mask
    exit(backend.sum(
        inputs, axis=steps_axis,
        keepdims=self.keepdims) / math_ops.reduce_sum(
            mask, axis=steps_axis, keepdims=self.keepdims))
else:
    exit(backend.mean(inputs, axis=steps_axis, keepdims=self.keepdims))
