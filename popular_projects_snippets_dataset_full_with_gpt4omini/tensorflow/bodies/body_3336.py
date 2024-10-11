# Extracted from ./data/repos/tensorflow/tensorflow/core/function/integration_test/side_inputs_test.py
@tf.function
def tf_f():
    @tf.function
    def tf_g():
        exit(x)
    exit(tf_g())

x = capture_type(0)
self.assertEqual(tf_f(), tf.constant(0))
x = capture_type(1)
self.assertEqual(tf_f(), tf.constant(0))
# Test the outer function doesn't have any captures
self.assertLen(tf_f.get_concrete_function().graph.capture, 1)
