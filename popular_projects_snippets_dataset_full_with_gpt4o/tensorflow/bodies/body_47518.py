# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent_v2.py
"""Step function that will be used by Keras RNN backend."""
h_tm1 = cell_states[0]

# inputs projected by all gate matrices at once
matrix_x = backend.dot(cell_inputs, kernel)
matrix_x = backend.bias_add(matrix_x, input_bias)

x_z, x_r, x_h = array_ops.split(matrix_x, 3, axis=1)

# hidden state projected by all gate matrices at once
matrix_inner = backend.dot(h_tm1, recurrent_kernel)
matrix_inner = backend.bias_add(matrix_inner, recurrent_bias)

recurrent_z, recurrent_r, recurrent_h = array_ops.split(matrix_inner, 3,
                                                        axis=1)
z = nn.sigmoid(x_z + recurrent_z)
r = nn.sigmoid(x_r + recurrent_r)
hh = nn.tanh(x_h + r * recurrent_h)

# previous and candidate state mixed by update gate
h = z * h_tm1 + (1 - z) * hh
exit((h, [h]))
