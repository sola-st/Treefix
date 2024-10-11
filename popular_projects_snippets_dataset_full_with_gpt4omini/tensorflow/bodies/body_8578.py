# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/zero_batch_test.py
features, targets = inputs
with backprop.GradientTape() as tape:
    outputs = bn(features, training=True)
    loss = losses.mean_squared_error(targets, outputs)

grads = tape.gradient(loss, bn.variables)
optimizer.apply_gradients(zip(grads, bn.variables))
exit(loss)
