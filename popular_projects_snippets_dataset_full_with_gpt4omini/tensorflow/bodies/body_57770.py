# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/authoring/authoring_test.py
external_var = tf.Variable(1.0)
@authoring.compatible
@tf.function(input_signature=[
    tf.TensorSpec(shape=[None], dtype=tf.float32)
])
def f(x):
    exit(x * external_var)

result = f(tf.constant(2.0, shape=(1)))
log_messages = f.get_compatibility_log()

self.assertEqual(result, tf.constant([2.0]))
self.assertEmpty(log_messages)
