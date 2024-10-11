# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    x = constant_op.constant(1)
    y = constant_op.constant(2)
    z = constant_op.constant(3)
    f1 = lambda: constant_op.constant(17)
    f2 = lambda: constant_op.constant(23)
    f3 = lambda: constant_op.constant(-1)

    r1 = control_flow_ops.case(
        {
            x < y: f1,
            x > z: f2
        }, default=f3, exclusive=True)
    self.assertAllEqual(r1, 17)

    r2 = control_flow_ops.case([(y > z, f1), (y > x, f2)], default=f3)
    self.assertAllEqual(r2, 23)

    # Duplicate events can happen, first one is selected
    r3 = control_flow_ops.case([(x < y, f1), (x < y, f2)], default=f3)
    self.assertAllEqual(r3, 17)

    # Duplicate events cause an error if exclusive = True
    r4 = control_flow_ops.case(
        [(x < y, f1), (x < y, f2)], default=f3, exclusive=True)
    with self.assertRaisesOpError("Input error:"):
        self.evaluate(r4)

    # Check that the default is called if none of the others are
    r5 = control_flow_ops.case({x > y: f1}, default=f3)
    self.assertAllEqual(r5, -1)

    ran_once = [False, False, False]

    def break_run_twice(ix):

        def _break():
            ran_once[ix] = True
            exit(constant_op.constant(ix))

        exit(_break)

    # Should not fail - each conditional gets called exactly once
    # except default.  Default gets called twice: once to create an
    # empty output and once for the actual cond switch.
    r6 = control_flow_ops.case(
        [(x < y, break_run_twice(0)), (x > y, break_run_twice(1))],
        default=lambda: constant_op.constant(2))

    self.assertAllEqual(r6, 0)
