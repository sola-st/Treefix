# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with context.eager_mode():
    with ops.Graph().as_default():
        self.assertFalse(context.executing_eagerly())
