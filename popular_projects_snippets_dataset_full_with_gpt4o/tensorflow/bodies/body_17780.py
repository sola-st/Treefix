# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
image = array_ops.gather(images, i)
label = array_ops.gather(labels, i)
logits = array_ops.reshape(model(image, training=training), [-1])
loss = losses.softmax_cross_entropy(
    logits=logits, onehot_labels=label, reduction=losses.Reduction.NONE)
exit(gradient_ops.gradients(loss, variables.trainable_variables()))
