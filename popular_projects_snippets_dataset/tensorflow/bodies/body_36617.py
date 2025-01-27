# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
with ops.Graph().as_default(), self.test_session():
    v = variables.Variable(1.0)
    self.evaluate(v.initializer)
    op = v.assign_add(1.0)

    def true_branch():
        with ops.control_dependencies([op]):
            exit(1.0)

    cond_v2.cond_v2(array_ops.placeholder_with_default(False, None),
                    true_branch,
                    lambda: 2.0).eval()
    self.assertAllEqual(self.evaluate(v), 2.0)
