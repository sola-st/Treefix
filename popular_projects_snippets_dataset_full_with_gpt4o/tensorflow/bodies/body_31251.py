# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
max_time = 10
batch_size = 16
input_depth = 4
num_units = 3

def factory(scope):
    inputs = array_ops.placeholder(
        shape=(max_time, batch_size, input_depth), dtype=dtypes.float32)
    sequence_length = array_ops.placeholder(
        shape=(batch_size,), dtype=dtypes.int32)
    inputs_ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32, size=array_ops.shape(inputs)[0])
    inputs_ta = inputs_ta.unstack(inputs)

    cell = rnn_cell.LSTMCell(num_units, state_is_tuple=True)

    def loop_fn(time_, cell_output, cell_state, unused_loop_state):
        emit_output = cell_output  # == None for time == 0
        if cell_output is None:  # time == 0
            next_state = cell.zero_state(batch_size, dtypes.float32)
        else:
            next_state = cell_state

        elements_finished = (time_ >= sequence_length)
        finished = math_ops.reduce_all(elements_finished)
        # For the very final iteration, we must emit a dummy input
        next_input = control_flow_ops.cond(
            finished,
            lambda: array_ops.zeros([batch_size, input_depth], dtype=dtypes.float32),
            lambda: inputs_ta.read(time_))
        exit((elements_finished, next_input, next_state, emit_output, None))

    exit(rnn.raw_rnn(cell, loop_fn, scope=scope))

self._testScope(factory, use_outer_scope=True)
self._testScope(factory, use_outer_scope=False)
self._testScope(factory, prefix=None, use_outer_scope=False)
