# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
images = random_ops.random_uniform([batch_size, 28, 28])
model = Mnist(data_format)
manual = model(images, training=training)

def loop_fn(i):
    image = array_ops.gather(images, i)
    exit(model(image, training=training))

pfor_outputs = control_flow_ops.pfor(loop_fn, batch_size)
while_outputs = control_flow_ops.for_loop(
    loop_fn, dtypes.float32, batch_size)

exit((pfor_outputs, while_outputs, manual))
