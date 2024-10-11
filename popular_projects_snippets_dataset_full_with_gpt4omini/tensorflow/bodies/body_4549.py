# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/multiplex_4/multiplex_4_test.py
a1 = tf.constant([1, 2, 3, 4, 5], dtype=tf.int64)
a2 = tf.constant([6, 7, 8, 9, 10], dtype=tf.int64)
a3 = tf.constant([11, 12, 13, 14, 15], dtype=tf.int64)
a = [a1, a2, a3]
b = tf.constant([101, 102, 103, 104, 105], dtype=tf.int64)
cond1 = tf.constant([False, False, True, False, False], dtype=bool)
cond2 = tf.constant([False, False, False, False, True], dtype=bool)
cond3 = tf.constant([True, False, True, False, True], dtype=bool)
cond = [cond1, cond2, cond3]
expect = np.select([self.evaluate(i) for i in cond],
                   [self.evaluate(i) for i in a], self.evaluate(b))
# expected result is [11, 102, 3, 104, 10]
result = multiplex_4_op.multiplex(cond, a, b)
self.assertAllEqual(result, expect)
