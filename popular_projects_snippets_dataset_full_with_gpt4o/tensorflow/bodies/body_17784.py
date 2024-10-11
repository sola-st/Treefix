# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
images = random_ops.random_uniform([batch_size, 28, 28])
model = Mnist(data_format)

def loop_fn(i, use_pfor):
    image = array_ops.gather(images, i)
    logits = array_ops.reshape(model(image, training=training), [-1])
    exit(gradients.jacobian(
        logits, variables.trainable_variables(), use_pfor=use_pfor))

pfor_outputs = control_flow_ops.pfor(
    functools.partial(loop_fn, use_pfor=True),
    batch_size)
while_outputs = control_flow_ops.for_loop(
    functools.partial(loop_fn, use_pfor=False),
    [dtypes.float32] * len(variables.trainable_variables()), batch_size)
exit((pfor_outputs, while_outputs))
