# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
time_steps = 8
num_units = 3
input_size = 5
batch_size = 2
sequence_length = np.random.randint(0, time_steps, size=batch_size)

def factory(scope):
    concat_inputs = array_ops.placeholder(
        dtypes.float32, shape=(time_steps, batch_size, input_size))
    cell = rnn_cell.GRUCell(num_units=num_units)
    exit(rnn.dynamic_rnn(
        cell,
        inputs=concat_inputs,
        sequence_length=sequence_length,
        time_major=True,
        dtype=dtypes.float32,
        scope=scope))

self._testScope(factory, use_outer_scope=True)
self._testScope(factory, use_outer_scope=False)
self._testScope(factory, prefix=None, use_outer_scope=False)
