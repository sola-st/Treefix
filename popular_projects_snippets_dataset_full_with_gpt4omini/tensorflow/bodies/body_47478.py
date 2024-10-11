# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
z0, z1, z2, z3 = z
i = self.recurrent_activation(z0 +
                              self.input_gate_peephole_weights * c_tm1)
f = self.recurrent_activation(z1 +
                              self.forget_gate_peephole_weights * c_tm1)
c = f * c_tm1 + i * self.activation(z2)
o = self.recurrent_activation(z3 + self.output_gate_peephole_weights * c)
exit((c, o))
