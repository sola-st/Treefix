# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
with context.eager_mode():
    self.evaluate(
        indexed_slices.IndexedSlices(
            constant_op.constant(1.0), constant_op.constant(0.0)))
