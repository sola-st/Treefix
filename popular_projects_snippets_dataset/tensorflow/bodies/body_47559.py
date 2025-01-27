# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional_recurrent.py
h_tm1 = states[0]  # previous memory state
c_tm1 = states[1]  # previous carry state

# dropout matrices for input units
dp_mask = self.get_dropout_mask_for_cell(inputs, training, count=4)
# dropout matrices for recurrent units
rec_dp_mask = self.get_recurrent_dropout_mask_for_cell(
    h_tm1, training, count=4)

if 0 < self.dropout < 1.:
    inputs_i = inputs * dp_mask[0]
    inputs_f = inputs * dp_mask[1]
    inputs_c = inputs * dp_mask[2]
    inputs_o = inputs * dp_mask[3]
else:
    inputs_i = inputs
    inputs_f = inputs
    inputs_c = inputs
    inputs_o = inputs

if 0 < self.recurrent_dropout < 1.:
    h_tm1_i = h_tm1 * rec_dp_mask[0]
    h_tm1_f = h_tm1 * rec_dp_mask[1]
    h_tm1_c = h_tm1 * rec_dp_mask[2]
    h_tm1_o = h_tm1 * rec_dp_mask[3]
else:
    h_tm1_i = h_tm1
    h_tm1_f = h_tm1
    h_tm1_c = h_tm1
    h_tm1_o = h_tm1

(kernel_i, kernel_f,
 kernel_c, kernel_o) = array_ops.split(self.kernel, 4, axis=3)
(recurrent_kernel_i,
 recurrent_kernel_f,
 recurrent_kernel_c,
 recurrent_kernel_o) = array_ops.split(self.recurrent_kernel, 4, axis=3)

if self.use_bias:
    bias_i, bias_f, bias_c, bias_o = array_ops.split(self.bias, 4)
else:
    bias_i, bias_f, bias_c, bias_o = None, None, None, None

x_i = self.input_conv(inputs_i, kernel_i, bias_i, padding=self.padding)
x_f = self.input_conv(inputs_f, kernel_f, bias_f, padding=self.padding)
x_c = self.input_conv(inputs_c, kernel_c, bias_c, padding=self.padding)
x_o = self.input_conv(inputs_o, kernel_o, bias_o, padding=self.padding)
h_i = self.recurrent_conv(h_tm1_i, recurrent_kernel_i)
h_f = self.recurrent_conv(h_tm1_f, recurrent_kernel_f)
h_c = self.recurrent_conv(h_tm1_c, recurrent_kernel_c)
h_o = self.recurrent_conv(h_tm1_o, recurrent_kernel_o)

i = self.recurrent_activation(x_i + h_i)
f = self.recurrent_activation(x_f + h_f)
c = f * c_tm1 + i * self.activation(x_c + h_c)
o = self.recurrent_activation(x_o + h_o)
h = o * self.activation(c)
exit((h, [h, c]))
