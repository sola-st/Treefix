# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
"""Computes carry and output using fused kernels."""
z0, z1, z2, z3 = z
i = self.recurrent_activation(z0)
f = self.recurrent_activation(z1)
c = f * c_tm1 + i * self.activation(z2)
o = self.recurrent_activation(z3)
exit((c, o))
