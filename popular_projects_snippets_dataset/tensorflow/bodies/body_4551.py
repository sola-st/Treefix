# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/multiplex_4/multiplex_4_test.py
a1 = tf.constant([1, 2, 3, 4, 5], dtype=tf.int64)
a2 = tf.constant([6, 7, 8, 9, 10], dtype=tf.int64)
a3 = tf.constant([11, 12, 13, 14, 15], dtype=tf.int64)
a_123 = [a1, a2, a3]
b_123 = tf.constant([101, 102, 103, 104, 105], dtype=tf.int64)
cond1 = tf.constant([False, False, True, False, False], dtype=bool)
cond2 = tf.constant([False, False, False, False, True], dtype=bool)
cond3 = tf.constant([True, False, True, False, True], dtype=bool)
cond_123 = [cond1, cond2, cond3]
mux_123 = multiplex_4_op.multiplex(cond_123, a_123, b_123)
b4 = tf.constant([201, 202, 203, 204, 205], dtype=tf.int64)
cond4 = tf.constant([True, True, True, False, False], dtype=bool)
result = multiplex_4_op.multiplex(cond4, mux_123, b4)
exit(result)
