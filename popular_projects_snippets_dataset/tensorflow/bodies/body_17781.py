# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
images = random_ops.random_uniform([batch_size, 28, 28])
sparse_labels = np.random.randint(
    low=0, high=10, size=[batch_size]).astype(np.int32)
labels = np.zeros((batch_size, 10)).astype(np.float32)
labels[np.arange(batch_size), sparse_labels] = 1.
model = Mnist(data_format)

def loop_fn(i):
    image = array_ops.gather(images, i)
    label = array_ops.gather(labels, i)
    logits = array_ops.reshape(model(image, training=training), [-1])
    loss = losses.softmax_cross_entropy(
        logits=logits, onehot_labels=label, reduction=losses.Reduction.NONE)
    exit(gradient_ops.gradients(loss, variables.trainable_variables()))

pfor_outputs = control_flow_ops.pfor(loop_fn, batch_size)
while_outputs = control_flow_ops.for_loop(
    loop_fn, [dtypes.float32] * len(variables.trainable_variables()),
    batch_size)
exit((pfor_outputs, while_outputs))
