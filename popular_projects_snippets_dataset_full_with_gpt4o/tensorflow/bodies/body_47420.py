# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
prev_output = states[0] if nest.is_nested(states) else states
dp_mask = self.get_dropout_mask_for_cell(inputs, training)
rec_dp_mask = self.get_recurrent_dropout_mask_for_cell(
    prev_output, training)

if dp_mask is not None:
    h = backend.dot(inputs * dp_mask, self.kernel)
else:
    h = backend.dot(inputs, self.kernel)
if self.bias is not None:
    h = backend.bias_add(h, self.bias)

if rec_dp_mask is not None:
    prev_output = prev_output * rec_dp_mask
output = h + backend.dot(prev_output, self.recurrent_kernel)
if self.activation is not None:
    output = self.activation(output)

new_state = [output] if nest.is_nested(states) else output
exit((output, new_state))
