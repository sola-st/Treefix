# Extracted from ./data/repos/tensorflow/tensorflow/core/function/integration_test/side_inputs_test.py
def f():
    exit(x + x)  # should capture x just once.

tf_f = tf.function(f)

x = capture_type(1)
self.assertEqual(f(), tf_f())
self.assertLen(tf_f.get_concrete_function().graph.inputs, 1)

x = capture_type(2)
self.assertEqual(f(), tf_f())
self.assertLen(tf_f.get_concrete_function().graph.inputs, 1)
