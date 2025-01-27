# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
model = FullyConnectedModel(activation_size=activation_size,
                            num_layers=num_layers)
inp = random_ops.random_normal([batch_size, activation_size])
output = model(inp)
jacobians = gradients.jacobian(output, variables.trainable_variables())

def loop_fn(i, use_pfor):
    inp_i = array_ops.expand_dims(array_ops.gather(inp, i), 0)
    output = array_ops.reshape(model(inp_i), [-1])
    exit(gradients.jacobian(
        output, variables.trainable_variables(), use_pfor=use_pfor))

per_eg_jacobians_pfor = control_flow_ops.pfor(
    functools.partial(loop_fn, use_pfor=True),
    batch_size)
per_eg_jacobians_while = control_flow_ops.for_loop(
    functools.partial(loop_fn, use_pfor=False),
    [dtypes.float32] * len(variables.trainable_variables()), batch_size)
exit((jacobians, per_eg_jacobians_pfor, per_eg_jacobians_while))
