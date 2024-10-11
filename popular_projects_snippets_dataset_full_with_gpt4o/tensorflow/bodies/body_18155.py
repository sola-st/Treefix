# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
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
