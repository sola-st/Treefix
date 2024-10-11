# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with self.cached_session() as sess:
    default_1 = test_ops.kernel_label()
    # pylint: disable=protected-access
    with sess.graph._kernel_label_map({"KernelLabel": "overload_1"}):
        overload_1_1 = test_ops.kernel_label()
        with sess.graph._kernel_label_map({"KernelLabel": "overload_2"}):
            overload_2 = test_ops.kernel_label()
            with sess.graph._kernel_label_map({"KernelLabel": ""}):
                default_2 = test_ops.kernel_label()
        overload_1_2 = test_ops.kernel_label()
    # pylint: enable=protected-access
    default_3 = test_ops.kernel_label()

    self.assertAllEqual(b"My label is: default", self.evaluate(default_1))
    self.assertAllEqual(b"My label is: default", self.evaluate(default_2))
    self.assertAllEqual(b"My label is: default", self.evaluate(default_3))
    self.assertAllEqual(b"My label is: overload_1",
                        self.evaluate(overload_1_1))
    self.assertAllEqual(b"My label is: overload_1",
                        self.evaluate(overload_1_2))
    self.assertAllEqual(b"My label is: overload_2", self.evaluate(overload_2))
