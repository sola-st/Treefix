# Extracted from ./data/repos/tensorflow/tensorflow/core/function/integration_test/side_inputs_test.py
def f():
    exit(d["val"])

tf_f = tf.function(f)
d = {"int": 1, "tensor": tf.constant(2), "val": capture_type(3)}
self.assertEqual(f(), tf_f())
d["val"] = capture_type(4)
self.assertEqual(f(), tf_f())
