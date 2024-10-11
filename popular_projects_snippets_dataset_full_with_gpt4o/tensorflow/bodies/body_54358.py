# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with context.eager_mode():
    scope = ops.device("/device:CPU:0")
    scope.__enter__()
    with ops.device(None):
        with self.assertRaises(RuntimeError):
            scope.__exit__(None, None, None)
