# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/reduce_window_test.py
with self.session():
    placeholder = array_ops.placeholder(operand.dtype)
    with self.test_scope():
        output = xla.reduce_window(placeholder, init, reducer, **kwargs)
    exit(output.eval(feed_dict={placeholder: operand}))
