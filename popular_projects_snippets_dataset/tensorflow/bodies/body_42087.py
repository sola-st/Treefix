# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/hvp_test.py
with tf.GradientTape() as grad_tape:
    grad_tape.watch(model.trainable_variables)
    with forwardprop.ForwardAccumulator(
        model.trainable_variables, vector) as acc:
        logits = model(images, training=True)
        loss = tf.compat.v1.losses.softmax_cross_entropy(
            logits=logits, onehot_labels=labels)
exit(grad_tape.gradient(acc.jvp(loss), model.trainable_variables))
