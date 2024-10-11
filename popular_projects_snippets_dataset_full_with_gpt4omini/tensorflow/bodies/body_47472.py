# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
h_tm1 = states[0]  # previous memory state
c_tm1 = states[1]  # previous carry state

dp_mask = self.get_dropout_mask_for_cell(inputs, training, count=4)
rec_dp_mask = self.get_recurrent_dropout_mask_for_cell(
    h_tm1, training, count=4)

if self.implementation == 1:
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
    k_i, k_f, k_c, k_o = array_ops.split(
        self.kernel, num_or_size_splits=4, axis=1)
    x_i = backend.dot(inputs_i, k_i)
    x_f = backend.dot(inputs_f, k_f)
    x_c = backend.dot(inputs_c, k_c)
    x_o = backend.dot(inputs_o, k_o)
    if self.use_bias:
        b_i, b_f, b_c, b_o = array_ops.split(
            self.bias, num_or_size_splits=4, axis=0)
        x_i = backend.bias_add(x_i, b_i)
        x_f = backend.bias_add(x_f, b_f)
        x_c = backend.bias_add(x_c, b_c)
        x_o = backend.bias_add(x_o, b_o)

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
    x = (x_i, x_f, x_c, x_o)
    h_tm1 = (h_tm1_i, h_tm1_f, h_tm1_c, h_tm1_o)
    c, o = self._compute_carry_and_output(x, h_tm1, c_tm1)
else:
    if 0. < self.dropout < 1.:
        inputs = inputs * dp_mask[0]
    z = backend.dot(inputs, self.kernel)
    z += backend.dot(h_tm1, self.recurrent_kernel)
    if self.use_bias:
        z = backend.bias_add(z, self.bias)

    z = array_ops.split(z, num_or_size_splits=4, axis=1)
    c, o = self._compute_carry_and_output_fused(z, c_tm1)

h = o * self.activation(c)
exit((h, [h, c]))
