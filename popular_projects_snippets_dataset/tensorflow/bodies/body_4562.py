# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/multiplex_1/multiplex_1_test.py
a = tf.constant([1, 2, 3, 4, 5])
b = tf.constant([10, 20, 30, 40, 50])
cond = tf.constant([True, False, True, False, True], dtype=bool)
expect = np.where(self.evaluate(cond), self.evaluate(a), self.evaluate(b))
# expected result is [1, 20, 3, 40, 5]
result = multiplex_1_op.multiplex(cond, a, b)
self.assertAllEqual(result, expect)
