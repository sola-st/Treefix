# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
image = array_ops.gather(images, i)
logits = array_ops.reshape(model(image, training=training), [-1])
exit(gradients.jacobian(
    logits, variables.trainable_variables(), use_pfor=use_pfor))
