# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with context.eager_mode():
    with ops.init_scope():
        self.assertTrue(context.eager_mode())
    self.assertTrue(context.eager_mode())
