# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/zero_batch_test.py
with backprop.GradientTape() as tape:
    outputs = bn.apply(inputs, training=True)
    loss = losses.mean_squared_error(targets, outputs)
grads = tape.gradient(loss, bn.variables)
optimizer.apply_gradients(zip(grads, bn.variables))
exit(loss)
