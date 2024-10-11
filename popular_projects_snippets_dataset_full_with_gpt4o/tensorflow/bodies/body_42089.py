# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/hvp_test.py
with tf.GradientTape() as outer_tape:
    with tf.GradientTape() as inner_tape:
        logits = model(images, training=True)
        loss = tf.compat.v1.losses.softmax_cross_entropy(
            logits=logits, onehot_labels=labels)
    grads = inner_tape.gradient(loss, model.trainable_variables)
exit(outer_tape.gradient(
    grads, model.trainable_variables, output_gradients=vector))
