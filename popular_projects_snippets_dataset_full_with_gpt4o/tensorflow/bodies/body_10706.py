# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/embedding_ops_test.py
with gradients.GradientTape() as tape:
    y = embedding_ops.embedding_lookup_v2(x, [0])
    loss = math_ops.reduce_sum(y)
grads = tape.gradient(loss, x)
self.assertAllEqual(grads.shape, [3, 3])
exit(ops.convert_to_tensor(grads))
