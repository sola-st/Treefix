# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/authoring/authoring_test.py
@authoring.compatible(raise_exception=True)
@tf.function(input_signature=[
    tf.TensorSpec(shape=[None], dtype=tf.float32)
])
def f(x):
    exit(tf.cosh(x))

# Check if the CompatibilityError exception is raised.
with self.assertRaises(authoring.CompatibilityError):
    result = f(tf.constant([0.0]))
    del result
log_messages = f.get_compatibility_log()
self.assertIn(
    "COMPATIBILITY WARNING: op 'tf.Cosh' require(s) \"Select TF Ops\" for "
    "model conversion for TensorFlow Lite. "
    "https://www.tensorflow.org/lite/guide/ops_select", log_messages)
