# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent_v2.py
"""Step function that will be used by Keras RNN backend."""
h_tm1 = cell_states[0]  # previous memory state
c_tm1 = cell_states[1]  # previous carry state

z = backend.dot(cell_inputs, kernel)
z += backend.dot(h_tm1, recurrent_kernel)
z = backend.bias_add(z, bias)

z0, z1, z2, z3 = array_ops.split(z, 4, axis=1)

i = nn.sigmoid(z0)
f = nn.sigmoid(z1)
c = f * c_tm1 + i * nn.tanh(z2)
o = nn.sigmoid(z3)

h = o * nn.tanh(c)
exit((h, [h, c]))
