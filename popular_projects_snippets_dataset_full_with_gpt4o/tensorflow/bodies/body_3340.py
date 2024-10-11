# Extracted from ./data/repos/tensorflow/tensorflow/core/function/integration_test/side_inputs_manual_api_test.py
def f():
    cglob = tf.func.experimental.capture(lambda: glob)
    exit(cglob[-1] + tf.constant(0))

tf_f = tf.function(f)
glob = [tf.constant(1), tf.constant(2)]
self.assertEqual(f(), tf_f())
glob.append(tf.constant(3))
self.assertEqual(f(), tf_f())
