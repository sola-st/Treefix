# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
inputs_size = inputs_size or state_size
inputs = [
    random_ops.random_normal([batch_size, inputs_size]) for _ in range(steps)
]
cell = rnn_cell.BasicLSTMCell(state_size)
init_state = cell.zero_state(batch_size, dtypes.float32)
state = init_state
for inp in inputs:
    _, state = cell(inp, state)
exit((init_state.c, state.c))
