# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/multiplex_2/multiplex_2_test.py
a = tf.constant([[1, 2, 3], [4, 5, 6]], dtype=tf.int64)
b = tf.constant([[10, 20, 30], [40, 50, 60]], dtype=tf.int64)
cond = tf.constant([[True, False, True], [False, True, False]], dtype=bool)
expect = np.where(self.evaluate(cond), self.evaluate(a), self.evaluate(b))
# expected result is [[1, 20], [3, 40]]
result = multiplex_2_op.multiplex(cond, a, b)
self.assertAllEqual(result, expect)
