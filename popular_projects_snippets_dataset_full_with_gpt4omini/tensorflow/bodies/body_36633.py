# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
with ops.Graph().as_default():
    _, cond_op = self._createCond(None)
    self.assertEqual(cond_op.name, "cond")
    self.assertRegex(cond_op.get_attr("then_branch").name, r"cond_true_\d*")
    self.assertRegex(cond_op.get_attr("else_branch").name, r"cond_false_\d*")

with ops.Graph().as_default():
    with ops.name_scope("foo"):
        _, cond1_op = self._createCond("")
        self.assertEqual(cond1_op.name, "foo/cond")
        self.assertRegex(
            cond1_op.get_attr("then_branch").name, r"foo_cond_true_\d*")
        self.assertRegex(
            cond1_op.get_attr("else_branch").name, r"foo_cond_false_\d*")

        _, cond2_op = self._createCond(None)
        self.assertEqual(cond2_op.name, "foo/cond_1")
        self.assertRegex(
            cond2_op.get_attr("then_branch").name, r"foo_cond_1_true_\d*")
        self.assertRegex(
            cond2_op.get_attr("else_branch").name, r"foo_cond_1_false_\d*")
