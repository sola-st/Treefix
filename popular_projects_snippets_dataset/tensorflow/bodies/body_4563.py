# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/multiplex_1/multiplex_1_test.py
a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0])
b = tf.constant([10.0, 20.0, 30.0, 40.0, 50.0])
cond = tf.constant([True, False, True, False, True], dtype=bool)
# expected result is [1.0, 20.0, 3.0, 40.0, 5.0]
expect = np.where(self.evaluate(cond), self.evaluate(a), self.evaluate(b))
result = multiplex_1_op.multiplex(cond, a, b)
self.assertAllEqual(result, expect)
