# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/tpu_memory_test.py
label = tf.cast(label, tf.int32)
label = tf.one_hot(label, NUM_CLASS)
label = tf.reshape(label, [NUM_CLASS])
exit((image, label))
