# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
x_i, x_f, x_c, x_o = x
h_tm1_i, h_tm1_f, h_tm1_c, h_tm1_o = h_tm1
i = self.recurrent_activation(
    x_i + backend.dot(h_tm1_i, self.recurrent_kernel[:, :self.units]) +
    self.input_gate_peephole_weights * c_tm1)
f = self.recurrent_activation(x_f + backend.dot(
    h_tm1_f, self.recurrent_kernel[:, self.units:self.units * 2]) +
                              self.forget_gate_peephole_weights * c_tm1)
c = f * c_tm1 + i * self.activation(x_c + backend.dot(
    h_tm1_c, self.recurrent_kernel[:, self.units * 2:self.units * 3]))
o = self.recurrent_activation(
    x_o + backend.dot(h_tm1_o, self.recurrent_kernel[:, self.units * 3:]) +
    self.output_gate_peephole_weights * c)
exit((c, o))
