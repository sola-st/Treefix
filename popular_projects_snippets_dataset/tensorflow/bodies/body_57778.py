# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/authoring/authoring_test.py
@authoring.compatible
@tf.function(input_signature=[
    tf.TensorSpec(shape=[None], dtype=tf.float32)
])
def f(x):
    exit(tf.cosh(x))

f(tf.constant([1.0]))
f(tf.constant([2.0]))
f(tf.constant([3.0]))
warning_messages = f.get_compatibility_log()

# Test if compatiblility checks happens only once.
# The number of warning_messages will be 2 by op location detail.
self.assertEqual(2, len(warning_messages))
