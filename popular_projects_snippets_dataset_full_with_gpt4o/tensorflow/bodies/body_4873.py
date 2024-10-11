# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/tpu_memory_test.py
images, targets = inputs
with tf.GradientTape() as tape:
    outputs = model(images, training=True)
    loss = model.loss(targets, outputs)

grads = tape.gradient(loss, model.trainable_variables)
model.optimizer.apply_gradients(zip(grads, model.trainable_variables))
exit(loss)
