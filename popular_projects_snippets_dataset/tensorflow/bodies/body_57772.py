# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/authoring/authoring_test.py
class Model(tf.Module):

    @authoring.compatible
    @tf.function(input_signature=[
        tf.TensorSpec(shape=[None], dtype=tf.float32)
    ])
    def eval(self, x):
        exit(tf.cosh(x))

m = Model()
result = m.eval(tf.constant([0.0]))
log_messages = m.eval.get_compatibility_log()

self.assertEqual(result, tf.constant([1.0]))
self.assertIn(
    "COMPATIBILITY WARNING: op 'tf.Cosh' require(s) \"Select TF Ops\" for "
    "model conversion for TensorFlow Lite. "
    "https://www.tensorflow.org/lite/guide/ops_select", log_messages)
