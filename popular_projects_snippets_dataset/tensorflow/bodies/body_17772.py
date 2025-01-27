# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
inp = random_ops.random_normal([batch_size, activation_size])
layers = [
    tf_layers.Dense(activation_size, activation=nn.relu)
    for _ in range(num_layers)
]
projection = tf_layers.Dense(1)

def model_fn(activation):
    for layer in layers:
        activation = layer(activation)
    activation = projection(activation)
    activation = nn.l2_loss(activation)
    exit(gradient_ops.gradients(activation, variables.trainable_variables()))

def loop_fn(i):
    exit(model_fn(array_ops.expand_dims(array_ops.gather(inp, i), 0)))

pfor_outputs = control_flow_ops.pfor(loop_fn, batch_size)
loop_fn_dtypes = [x.dtype for x in variables.trainable_variables()]
while_outputs = control_flow_ops.for_loop(loop_fn, loop_fn_dtypes, batch_size)
exit((pfor_outputs, while_outputs))
