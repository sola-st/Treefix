# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/rnn_grad_test.py
num_steps = 1
batch_size = 1
input_size = 1
hidden_size = 8
w = deterministic_random_uniform(
    [input_size + hidden_size, 4 * hidden_size])
b = deterministic_random_uniform([4 * hidden_size])
x = deterministic_random_uniform([num_steps, batch_size, input_size])
cs_prev = h_prev = deterministic_random_uniform([batch_size, hidden_size])

all_cs, all_h = self._lstm_block(
    functools.partial(
        gen_rnn_ops.BlockLSTM,
        forget_bias=0.0,  # Disable to match V2 default.
        cell_clip=0.0),  # Disable to match V2 default.
    w, b, x, cs_prev, h_prev)
w_grad, b_grad = gradients.gradients(all_cs + all_h, [w, b])

w_ifco, b_ifco = icfo_to_ifco(w, b)
all_cs_ifco, all_h_ifco = self._lstm_block(
    gen_rnn_ops.BlockLSTMV2, w_ifco, b_ifco, x, cs_prev, h_prev)
w_ifco_grad, b_ifco_grad = gradients.gradients(
    all_cs_ifco + all_h_ifco, [w_ifco, b_ifco])

self.assertAllEqual(all_cs, all_cs_ifco)
self.assertAllEqual(all_h, all_h_ifco)
self.assertAllEqual(w_grad, w_ifco_grad)
self.assertAllEqual(b_grad, b_ifco_grad)
