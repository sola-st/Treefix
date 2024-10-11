# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/rnn_grad_test.py
batch_size = np.random.randint(1, 32)
input_size = np.random.randint(1, 32)
hidden_size = np.random.randint(1, 32)
w = deterministic_random_uniform(
    [input_size + hidden_size, 4 * hidden_size])
b = deterministic_random_uniform([4 * hidden_size])
x = deterministic_random_uniform([batch_size, input_size])
cs_prev = h_prev = deterministic_random_uniform([batch_size, hidden_size])
w_peephole = array_ops.zeros(cs_prev.shape[1:], dtype=w.dtype)
cs_grad = deterministic_random_uniform([batch_size, hidden_size])
h_grad = deterministic_random_uniform([batch_size, hidden_size])

outputs = []
grads = []
for use_gpu in [False, True]:
    with self.cached_session(use_gpu=use_gpu):
        output = gen_rnn_ops.lstm_block_cell(
            x=x,
            cs_prev=cs_prev,
            h_prev=h_prev,
            w=w,
            wci=w_peephole,
            wcf=w_peephole,
            wco=w_peephole,
            b=b,
            forget_bias=1.0,
            cell_clip=0.0,
            use_peephole=False)
        (i, cs, f, o, ci, co, _) = output
        grad = gen_rnn_ops.lstm_block_cell_grad(
            x=x,
            cs_prev=cs_prev,
            h_prev=h_prev,
            w=w,
            wci=w_peephole,
            wcf=w_peephole,
            wco=w_peephole,
            b=b,
            i=i,
            cs=cs,
            f=f,
            o=o,
            ci=ci,
            co=co,
            cs_grad=cs_grad,
            h_grad=h_grad,
            use_peephole=False)
        outputs.append(output)
        grads.append(grad)
self.assertAllClose(outputs[0], outputs[1])
self.assertAllClose(grads[0], grads[1])
