# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/hvp_test.py
with tf.GradientTape() as grad_tape:
    logits = model(images, training=True)
    loss = tf.compat.v1.losses.softmax_cross_entropy(
        logits=logits, onehot_labels=labels)
variables = model.trainable_variables
grads = grad_tape.gradient(loss, variables)
helpers = tf.nest.map_structure(tf.ones_like, grads)
transposing = tf.gradients(grads, variables, helpers)
exit(tf.gradients(transposing, helpers, vector))
