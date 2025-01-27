# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/tpu_memory_test.py
image = tf.ones([500, 500, 3], dtype=tf.float32)
label = tf.zeros([1], dtype=tf.int32)
exit((image, label))
