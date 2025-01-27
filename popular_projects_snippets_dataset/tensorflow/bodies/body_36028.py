# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode():
    v = resource_variable_ops.ResourceVariable(1)
    text = "%r" % v
    self.assertEqual(
        "<tf.Variable 'Variable:0' shape=() dtype=int32, numpy=1>", text)
