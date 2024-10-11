# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
forget_bias = 1
cell_clip = 0
use_peephole = False
x = constant_op.constant(0.837607, shape=[28, 29], dtype=dtypes.float32)
cs_prev = constant_op.constant(0, shape=[28, 17], dtype=dtypes.float32)
h_prev = constant_op.constant(
    0.592631638, shape=[28, 17], dtype=dtypes.float32)
w = constant_op.constant(0.887386262, shape=[46, 68], dtype=dtypes.float32)
wci = constant_op.constant(0, shape=[], dtype=dtypes.float32)
wcf = constant_op.constant(0, shape=[17], dtype=dtypes.float32)
wco = constant_op.constant(
    0.592631638, shape=[28, 17], dtype=dtypes.float32)
b = constant_op.constant(0.75259006, shape=[68], dtype=dtypes.float32)
with self.assertRaises(errors_impl.InvalidArgumentError):
    self.evaluate(
        gen_rnn_ops.lstm_block_cell(
            x=x,
            cs_prev=cs_prev,
            h_prev=h_prev,
            w=w,
            wci=wci,
            wcf=wcf,
            wco=wco,
            b=b,
            forget_bias=forget_bias,
            cell_clip=cell_clip,
            use_peephole=use_peephole))
