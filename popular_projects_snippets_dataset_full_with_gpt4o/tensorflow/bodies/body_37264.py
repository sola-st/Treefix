# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
for v1_first in [True, False]:
    with self.cached_session():
        v1 = variables.VariableV1([1.0])
        add1 = math_ops.add(
            control_flow_ops.with_dependencies([v1.initializer], v1._ref()),  # pylint: disable=protected-access
            2.0)
        v2 = variables.VariableV1([10.0])
        add2 = math_ops.add(
            control_flow_ops.with_dependencies([v2.initializer], v2._ref()),  # pylint: disable=protected-access
            20.0)
        t1, _, t2 = control_flow_ops.tuple([add1, None, add2])

        # v1 is not initialized.
        with self.assertRaisesOpError("Attempting to use uninitialized value"):
            self.evaluate(v1)

        # v2 is not initialized.
        with self.assertRaisesOpError("Attempting to use uninitialized value"):
            self.evaluate(v2)

        if v1_first:
            # Getting t1 initializes v2.
            self.assertAllClose([3.0], self.evaluate(t1))
            self.assertAllClose([10.0], self.evaluate(v2))
        else:
            # Getting t2 initializes v1.
            self.assertAllClose([30.0], self.evaluate(t2))
            self.assertAllClose([1.0], self.evaluate(v1))
