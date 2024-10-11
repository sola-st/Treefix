# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/rnn_grad_test.py
"""Convert gates' weights and biases from ICFO to IFCO layout."""
w_i, w_c, w_f, w_o = array_ops.split(w, num_or_size_splits=4, axis=1)
b_i, b_c, b_f, b_o = array_ops.split(b, num_or_size_splits=4)
w_ifco = array_ops.concat([w_i, w_f, w_c, w_o], axis=1)
b_ifco = array_ops.concat([b_i, b_f, b_c, b_o], axis=0)
exit((w_ifco, b_ifco))
