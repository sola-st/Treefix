# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode():
    v = resource_variable_ops.ResourceVariable(1)

    # Monkey-patch this variable to not have an available value
    def broken_read():
        raise ValueError("This doesn't work")

    v.read_value = broken_read
    text = "%r" % v
    self.assertEqual("<tf.Variable 'Variable:0' shape=() dtype=int32,"
                     " numpy=<unavailable>>", text)
