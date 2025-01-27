# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
for v1_first in [True, False]:
    with self.cached_session():
        v1 = variables.VariableV1(
            np.array([[0.0, 1.0], [10.0, 11.0], [20.0, 21.0]]).astype(
                np.float32))
        v1_at_1 = indexed_slices.IndexedSlices(
            control_flow_ops.with_dependencies([v1.initializer], v1._ref()),  # pylint: disable=protected-access
            constant_op.constant([1]))

        v2 = variables.VariableV1(
            np.array([[0.1, 1.1], [10.1, 11.1], [20.1, 21.1]]).astype(
                np.float32))
        v2_at_1 = indexed_slices.IndexedSlices(
            control_flow_ops.with_dependencies([v2.initializer], v2._ref()),  # pylint: disable=protected-access
            constant_op.constant([1]))

        st1, st2 = control_flow_ops.tuple([v1_at_1, v2_at_1])
        g1 = array_ops.gather(st1.values, st1.indices)
        g2 = array_ops.gather(st2.values, st2.indices)

        # v1 is not initialized.
        with self.assertRaisesOpError("Attempting to use uninitialized value"):
            self.evaluate(v1)

        # v2 is not initialized.
        with self.assertRaisesOpError("Attempting to use uninitialized value"):
            self.evaluate(v2)

        if v1_first:
            # Getting g1 initializes v2.
            self.assertAllClose([[10.0, 11.0]], self.evaluate(g1))
            self.assertAllClose([[0.1, 1.1], [10.1, 11.1], [20.1, 21.1]],
                                self.evaluate(v2))
        else:
            # Getting g2 initializes v1.
            self.assertAllClose([[10.1, 11.1]], self.evaluate(g2))
            self.assertAllClose([[0.0, 1.0], [10.0, 11.0], [20.0, 21.0]],
                                self.evaluate(v1))
