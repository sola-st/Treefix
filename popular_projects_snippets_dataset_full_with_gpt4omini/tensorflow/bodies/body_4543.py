# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/multiplex_4/model_using_multiplex.py
cond = tf.constant([True, False, True, False, True], dtype=bool)
a = tf.constant([1, 2, 3, 4, 5], dtype=tf.int64)
b = tf.constant([10, 20, 30, 40, 50], dtype=tf.int64)
exit((cond, a, b))
