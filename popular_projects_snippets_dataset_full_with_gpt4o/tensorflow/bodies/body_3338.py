# Extracted from ./data/repos/tensorflow/tensorflow/core/function/integration_test/side_inputs_manual_api_test.py
def f():
    exit(tf.func.experimental.capture(lambda: x) + 1)

tf_f = tf.function(f)
x = type_before(val_before)
self.assertEqual(f(), tf_f())
x = type_after(val_after)
self.assertEqual(f(), tf_f())
