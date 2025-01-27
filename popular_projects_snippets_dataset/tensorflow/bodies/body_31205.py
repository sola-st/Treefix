# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
use_peephole = False
seq_len_max = constant_op.constant(1, shape=[], dtype=dtypes.int64)
x = constant_op.constant(0.504355371, shape=[1, 1, 1], dtype=dtypes.float32)
cs_prev = constant_op.constant(
    0.504355371, shape=[1, 1, 1], dtype=dtypes.float32)
h_prev = constant_op.constant(
    0.504355371, shape=[1, 1], dtype=dtypes.float32)
w = constant_op.constant(0.504355371, shape=[1, 1], dtype=dtypes.float32)
wci = constant_op.constant(0.504355371, shape=[1], dtype=dtypes.float32)
wcf = constant_op.constant(0.504355371, shape=[1], dtype=dtypes.float32)
wco = constant_op.constant(0.504355371, shape=[1], dtype=dtypes.float32)
b = constant_op.constant(0.504355371, shape=[1], dtype=dtypes.float32)
i = constant_op.constant(0.504355371, shape=[1, 1, 1], dtype=dtypes.float32)
cs = constant_op.constant(
    0.504355371, shape=[1, 1, 1], dtype=dtypes.float32)
f = constant_op.constant(0.504355371, shape=[1, 1, 1], dtype=dtypes.float32)
o = constant_op.constant(0.504355371, shape=[1, 1, 1], dtype=dtypes.float32)
ci = constant_op.constant(
    0.504355371, shape=[1, 1, 1], dtype=dtypes.float32)
co = constant_op.constant(
    0.504355371, shape=[1, 1, 1], dtype=dtypes.float32)
h = constant_op.constant(0.504355371, shape=[1, 1, 1], dtype=dtypes.float32)
cs_grad = constant_op.constant(
    0.504355371, shape=[1, 1, 1], dtype=dtypes.float32)
h_grad = constant_op.constant(
    0.504355371, shape=[1, 1, 1], dtype=dtypes.float32)
with self.assertRaisesRegex((ValueError, errors_impl.InvalidArgumentError),
                            "must be rank"):
    self.evaluate(
        gen_rnn_ops.block_lstm_grad_v2(
            seq_len_max=seq_len_max,
            x=x,
            cs_prev=cs_prev,
            h_prev=h_prev,
            w=w,
            wci=wci,
            wcf=wcf,
            wco=wco,
            b=b,
            i=i,
            cs=cs,
            f=f,
            o=o,
            ci=ci,
            co=co,
            h=h,
            cs_grad=cs_grad,
            h_grad=h_grad,
            use_peephole=use_peephole))
