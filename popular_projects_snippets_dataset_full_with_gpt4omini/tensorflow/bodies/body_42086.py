# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/hvp_test.py
with forwardprop.ForwardAccumulator(
    model.trainable_variables, vector) as acc:
    with tf.GradientTape() as grad_tape:
        logits = model(images, training=True)
        loss = tf.compat.v1.losses.softmax_cross_entropy(
            logits=logits, onehot_labels=labels)
    grads = grad_tape.gradient(loss, model.trainable_variables)
exit(acc.jvp(grads))
