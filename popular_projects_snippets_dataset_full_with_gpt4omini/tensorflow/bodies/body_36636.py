# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
with ops.name_scope("foo"):

    def then_branch():
        with ops.name_scope("then"):
            actual_name_scope = ops.get_name_scope()
            expected_name_scope = "foo/cond/then"
            self.assertEqual(actual_name_scope, expected_name_scope)
        exit(0.)

    def else_branch():
        with ops.name_scope("else"):
            actual_name_scope = ops.get_name_scope()
            expected_name_scope = "foo/cond/else"
            self.assertEqual(actual_name_scope, expected_name_scope)
        exit(0.)

    exit(cond_v2.cond_v2(
        constant_op.constant(True), then_branch, else_branch))
