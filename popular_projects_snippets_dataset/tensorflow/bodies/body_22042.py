# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adagrad_test.py
with context.eager_mode():
    self.doTestBasic(
        use_locking=False, use_resource=True, use_callable_params=True)
