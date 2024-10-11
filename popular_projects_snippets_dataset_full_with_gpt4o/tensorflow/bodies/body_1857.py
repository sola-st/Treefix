# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sharding_util_ops_test.py
num_partitions = [2] * rank
shape = [4] * rank
value = np.arange(0, np.prod(shape)).reshape(shape)
for dtype in self.numeric_types:
    with self.session() as sess, self.device_scope():
        validate = graph_fn(sess, value, dtype, num_partitions)
        result = sess.run(validate)
    self.assertAllEqual(result, np.broadcast_to(True, shape))
