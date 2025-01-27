# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/saved_model_test.py
self.v1 = tf.Variable([0, 0, 0, 0])
self.v2 = tf.Variable([1, 1, 1, 1])
self.table = lookup_ops.MutableHashTable(
    key_dtype=tf.int32, value_dtype=tf.int32, default_value=-1)
