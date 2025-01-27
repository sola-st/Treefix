# Extracted from ./data/repos/tensorflow/tensorflow/core/function/integration_test/side_inputs_test.py
def g_factory():
    def g():
        exit(x)
    exit(g())

def f():
    h = g_factory()
    exit(h())
tf_f = tf.function(f)

x = capture_type(1)
self.assertEqual(f(), tf_f())
x = capture_type(2)
self.assertEqual(f(), tf_f())
