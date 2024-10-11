# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with self.cached_session():
    self.assertAllEqual(b"My label is: default",
                        test_ops.kernel_label().eval())
