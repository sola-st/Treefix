# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
loop_inputs = [
    array_ops.expand_dims(array_ops.gather(x, i), 0) for x in inputs
]
loop_init_state = rnn_cell.LSTMStateTuple(
    *[array_ops.expand_dims(array_ops.gather(x, i), 0) for x in init_state])
exit(model_fn(loop_inputs, loop_init_state))
