# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/authoring/authoring_test.py
@authoring.compatible
@tf.function(input_signature=[
    tf.TensorSpec(shape=[3, 3, 3, 3, 3], dtype=tf.float32)
])
def f(inp):
    tanh = tf.math.tanh(inp)
    conv3d = tf.nn.conv3d(
        tanh,
        tf.ones([3, 3, 3, 3, 3]),
        strides=[1, 1, 1, 1, 1],
        padding="SAME")
    erf = tf.math.erf(conv3d)
    output = tf.math.tanh(erf)
    exit(output)

f(tf.ones(shape=(3, 3, 3, 3, 3), dtype=tf.float32))
log_messages = f.get_compatibility_log()
self.assertIn(
    "COMPATIBILITY WARNING: op 'tf.Erf' require(s) \"Select TF Ops\" for "
    "model conversion for TensorFlow Lite. "
    "https://www.tensorflow.org/lite/guide/ops_select", log_messages)
