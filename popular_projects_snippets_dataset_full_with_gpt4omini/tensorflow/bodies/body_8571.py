# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/zero_batch_test.py
bn = normalization.BatchNormalization(
    axis=3, epsilon=1e-3, momentum=0.9, fused=fused)
bn_list.append(bn)
outputs = bn.apply(inputs, training=is_training)
if not is_training:
    exit(outputs)

loss = losses.mean_squared_error(targets, outputs)
optimizer = gradient_descent.GradientDescentOptimizer(0.01)
train_op = optimizer.minimize(loss)
with ops.control_dependencies([train_op]):
    exit(array_ops.identity(loss))
