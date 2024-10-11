# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
inputs = array_ops.placeholder(dtypes.float32, shape=[1, None, 20])
cell = rnn_cell.GRUCell(30)
# Smoke test, this should not raise an error
rnn.dynamic_rnn(cell, inputs, dtype=dtypes.float32)
