# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
cell = cell_fn(state_size)
inputs, sequence_length = dynamic_lstm_input_fn(batch_size, state_size,
                                                max_steps)
inputs_ta = tensor_array_ops.TensorArray(
    dtypes.float32, size=max_steps, element_shape=[batch_size, state_size])
inputs_time_major = array_ops.transpose(inputs, [1, 0, 2])
inputs_ta = inputs_ta.unstack(inputs_time_major)
zeros = array_ops.zeros([state_size])

def loop_fn(i):
    sequence_length_i = array_ops.gather(sequence_length, i)

    def body_fn(t, state, ta):
        inputs_t = array_ops.expand_dims(
            array_ops.gather(inputs_ta.read(t), i), 0)
        output, new_state = cell(inputs_t, state)
        output = array_ops.reshape(output, [-1])
        # TODO(agarwal): one optimization that dynamic_rnn uses is to avoid the
        # array_ops.where when t < min(sequence_length). Doing that requires
        # supporting tf.cond pfor conversion.
        done = t >= sequence_length_i
        output = array_ops.where(done, zeros, output)
        ta = ta.write(t, output)
        new_state = [
            array_ops.where(done, s, ns)
            for s, ns in zip(nest.flatten(state), nest.flatten(new_state))
        ]
        new_state = nest.pack_sequence_as(state, new_state)
        exit((t + 1, new_state, ta))

    def condition_fn(t, _, unused):
        del unused
        exit(t < max_steps)

    initial_state = cell.zero_state(1, dtypes.float32)
    _, state, ta = control_flow_ops.while_loop(condition_fn, body_fn, [
        0, initial_state,
        tensor_array_ops.TensorArray(dtypes.float32, max_steps)
    ])

    new_state = [array_ops.reshape(x, [-1]) for x in nest.flatten(state)]
    new_state = nest.pack_sequence_as(initial_state, new_state)
    exit((ta.stack(), new_state))

pfor_output = pfor_control_flow_ops.pfor(loop_fn, batch_size)
tf_output = rnn.dynamic_rnn(
    cell,
    inputs,
    sequence_length=sequence_length,
    initial_state=cell.zero_state(batch_size, dtypes.float32))
exit((pfor_output, tf_output))
