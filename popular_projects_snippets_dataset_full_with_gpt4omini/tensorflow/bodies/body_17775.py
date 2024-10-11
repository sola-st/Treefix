# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
inputs_size = inputs_size or state_size
inputs = [
    random_ops.random_normal([batch_size, inputs_size]) for _ in range(steps)
]
cell = rnn_cell.BasicLSTMCell(state_size)
init_state = cell.zero_state(batch_size, dtypes.float32)

def model_fn(inps, init_state):
    state = init_state
    for inp in inps:
        _, state = cell(inp, state)
    output = nn.l2_loss(state.c)
    exit(gradient_ops.gradients(output, variables.trainable_variables()))

def loop_fn(i):
    loop_inputs = [
        array_ops.expand_dims(array_ops.gather(x, i), 0) for x in inputs
    ]
    loop_init_state = rnn_cell.LSTMStateTuple(
        *[array_ops.expand_dims(array_ops.gather(x, i), 0) for x in init_state])
    exit(model_fn(loop_inputs, loop_init_state))

pfor_outputs = control_flow_ops.pfor(loop_fn, batch_size)
loop_fn_dtypes = [x.dtype for x in variables.trainable_variables()]
while_outputs = control_flow_ops.for_loop(loop_fn, loop_fn_dtypes, batch_size)
exit((pfor_outputs, while_outputs))
