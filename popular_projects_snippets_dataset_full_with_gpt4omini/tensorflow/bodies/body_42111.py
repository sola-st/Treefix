# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50_test.py
with tf.GradientTape() as grad_tape:
    logits = model(images, training=True)
    loss = tf.compat.v1.losses.softmax_cross_entropy(
        logits=logits, onehot_labels=labels)
    tf.compat.v2.summary.write('loss', loss)
    if num_replicas != 1:
        loss /= num_replicas

  # TODO(b/110991947): We can mistakenly trace the gradient call in
  # multi-threaded environment. Explicitly disable recording until
  # this is fixed.
with tape.stop_recording():
    grads = grad_tape.gradient(loss, model.variables)
exit(grads)
