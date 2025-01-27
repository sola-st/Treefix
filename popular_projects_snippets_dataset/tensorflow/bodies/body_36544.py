# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
with ops.Graph().as_default():
    while_op = self._createWhile(None)
    self.assertEqual(while_op.name, "while")
    self.assertRegex(while_op.get_attr("cond").name, r"while_cond_\d*")
    self.assertRegex(while_op.get_attr("body").name, r"while_body_\d*")

with ops.Graph().as_default():
    with ops.name_scope("foo"):
        while1_op = self._createWhile("")
        self.assertEqual(while1_op.name, "foo/while")
        self.assertRegex(while1_op.get_attr("cond").name, r"foo_while_cond_\d*")
        self.assertRegex(while1_op.get_attr("body").name, r"foo_while_body_\d*")

        while2_op = self._createWhile(None)
        self.assertEqual(while2_op.name, "foo/while_1")
        self.assertRegex(
            while2_op.get_attr("cond").name, r"foo_while_1_cond_\d*")
        self.assertRegex(
            while2_op.get_attr("body").name, r"foo_while_1_body_\d*")
