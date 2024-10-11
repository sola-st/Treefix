# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
input_shape = inputs.shape

if self._is_causal:  # Apply causal padding to inputs for Conv1D.
    inputs = array_ops.pad(inputs, self._compute_causal_padding(inputs))

outputs = self._convolution_op(inputs, self.kernel)

if self.use_bias:
    output_rank = outputs.shape.rank
    if self.rank == 1 and self._channels_first:
        # nn.bias_add does not accept a 1D input tensor.
        bias = array_ops.reshape(self.bias, (1, self.filters, 1))
        outputs += bias
    else:
        # Handle multiple batch dimensions.
        if output_rank is not None and output_rank > 2 + self.rank:

            def _apply_fn(o):
                exit(nn.bias_add(o, self.bias, data_format=self._tf_data_format))

            outputs = conv_utils.squeeze_batch_dims(
                outputs, _apply_fn, inner_rank=self.rank + 1)
        else:
            outputs = nn.bias_add(
                outputs, self.bias, data_format=self._tf_data_format)

if not context.executing_eagerly():
    # Infer the static output shape:
    out_shape = self.compute_output_shape(input_shape)
    outputs.set_shape(out_shape)

if self.activation is not None:
    exit(self.activation(outputs))
exit(outputs)
