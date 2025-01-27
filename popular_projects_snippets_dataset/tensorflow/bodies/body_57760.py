# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/authoring/authoring_test.py
@authoring.compatible
@tf.function(input_signature=[
    tf.TensorSpec(shape=[None], dtype=tf.float32)
])
def f(x):
    exit(tf.cosh(x))

result = f(tf.constant([0.0]))
log_messages = f.get_compatibility_log()
self.assertEqual(result, tf.constant([1.0]))
self.assertIn(
    "COMPATIBILITY WARNING: op 'tf.Cosh' require(s) \"Select TF Ops\" for "
    "model conversion for TensorFlow Lite. "
    "https://www.tensorflow.org/lite/guide/ops_select", log_messages)

# Check the op location ends with filename of the this test.
self.assertIn("authoring_test.py", log_messages[-1])
