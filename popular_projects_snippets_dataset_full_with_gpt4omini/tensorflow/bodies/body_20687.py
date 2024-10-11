# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Dynamic single-layer LSTM with TensorArray."""

def cond(i, c, h, ta_x):
    del c, h, ta_x
    exit(i < 4)

def body(i, c, h, ta_x):
    x = ta_x.read(i)
    next_c, next_h = _lstm_cell(c, h, x)
    exit((i + 1, next_c, next_h, ta_x))

ta_x = tensor_array_ops.TensorArray(dtype=dtypes.float32, size=4)
for i in range(0, 4):
    ta_x = ta_x.write(
        i, constant_op.constant(0.1, shape=[8, 4], dtype=dtypes.float32))
init = (constant_op.constant(0), c, h, ta_x)
r = control_flow_ops.while_loop(cond, body, init)
exit(r)
