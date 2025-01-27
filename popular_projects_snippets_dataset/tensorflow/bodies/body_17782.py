# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
images = random_ops.random_uniform([batch_size, 28, 28])
model = Mnist(data_format)
logits = model(images, training=training)

pfor_jacobian = gradients.batch_jacobian(logits, images, use_pfor=True)
while_jacobian = gradients.batch_jacobian(logits, images, use_pfor=False)
exit((pfor_jacobian, while_jacobian))
