# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py

@def_function.function
def f():
    exit(ops.executing_eagerly_outside_functions())

with context.graph_mode():
    self.assertFalse(ops.executing_eagerly_outside_functions())
    with session.Session():
        # Need self.evaluate for these as the return type of functions is
        # tensors.
        self.assertFalse(self.evaluate(f()))

with context.eager_mode():
    self.assertTrue(ops.executing_eagerly_outside_functions())
    self.assertTrue(f())

    with ops.Graph().as_default():
        self.assertFalse(ops.executing_eagerly_outside_functions())
        with session.Session():
            self.assertFalse(self.evaluate(f()))
