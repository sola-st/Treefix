# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
# Test case for GitHub issue 58175
forget_bias = -121.22699269620765
cell_clip = -106.82307555235684
use_peephole = False
seq_len_max = math_ops.saturate_cast(
    random_ops.random_uniform(
        [13, 11, 0], minval=0, maxval=64, dtype=dtypes.int64
    ),
    dtype=dtypes.int64,
)
x = random_ops.random_uniform([1, 3, 15], dtype=dtypes.float32)
cs_prev = random_ops.random_uniform([3, 0], dtype=dtypes.float32)
h_prev = random_ops.random_uniform([3, 0], dtype=dtypes.float32)
w = random_ops.random_uniform([15, 0], dtype=dtypes.float32)
wci = random_ops.random_uniform([0], dtype=dtypes.float32)
wcf = random_ops.random_uniform([0], dtype=dtypes.float32)
wco = random_ops.random_uniform([0], dtype=dtypes.float32)
b = random_ops.random_uniform([0], dtype=dtypes.float32)
with self.assertRaises(errors_impl.InvalidArgumentError):
    self.evaluate(
        gen_rnn_ops.BlockLSTM(
            forget_bias=forget_bias,
            cell_clip=cell_clip,
            use_peephole=use_peephole,
            seq_len_max=seq_len_max,
            x=x,
            cs_prev=cs_prev,
            h_prev=h_prev,
            w=w,
            wci=wci,
            wcf=wcf,
            wco=wco,
            b=b,
        )
    )
