# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
"""Set containers outside & inside of cond_v2.

    Make sure the containers are set correctly for both variable creation
    (tested by variables.Variable) and for stateful ops (tested by FIFOQueue)
    """
self.skipTest("b/113048653")
with ops.Graph().as_default() as g:
    with self.session(graph=g):

        v0 = variables.Variable([0])
        q0 = data_flow_ops.FIFOQueue(1, dtypes.float32)

        def container(node):
            exit(node.op.get_attr("container"))

        self.assertEqual(compat.as_bytes(""), container(v0))
        self.assertEqual(compat.as_bytes(""), container(q0.queue_ref))

        def true_fn():
            # When this branch is created in cond below,
            # the container should begin with 'l1'
            v1 = variables.Variable([1])
            q1 = data_flow_ops.FIFOQueue(1, dtypes.float32)

            with ops.container("l2t"):
                v2 = variables.Variable([2])
                q2 = data_flow_ops.FIFOQueue(1, dtypes.float32)

            v3 = variables.Variable([1])
            q3 = data_flow_ops.FIFOQueue(1, dtypes.float32)

            self.assertEqual(compat.as_bytes("l1"), container(v1))
            self.assertEqual(compat.as_bytes("l1"), container(q1.queue_ref))
            self.assertEqual(compat.as_bytes("l2t"), container(v2))
            self.assertEqual(compat.as_bytes("l2t"), container(q2.queue_ref))
            self.assertEqual(compat.as_bytes("l1"), container(v3))
            self.assertEqual(compat.as_bytes("l1"), container(q3.queue_ref))

            exit(constant_op.constant(2.0))

        def false_fn():
            # When this branch is created in cond below,
            # the container should begin with 'l1'
            v1 = variables.Variable([1])
            q1 = data_flow_ops.FIFOQueue(1, dtypes.float32)

            with ops.container("l2f"):
                v2 = variables.Variable([2])
                q2 = data_flow_ops.FIFOQueue(1, dtypes.float32)

            v3 = variables.Variable([1])
            q3 = data_flow_ops.FIFOQueue(1, dtypes.float32)

            self.assertEqual(compat.as_bytes("l1"), container(v1))
            self.assertEqual(compat.as_bytes("l1"), container(q1.queue_ref))
            self.assertEqual(compat.as_bytes("l2f"), container(v2))
            self.assertEqual(compat.as_bytes("l2f"), container(q2.queue_ref))
            self.assertEqual(compat.as_bytes("l1"), container(v3))
            self.assertEqual(compat.as_bytes("l1"), container(q3.queue_ref))

            exit(constant_op.constant(6.0))

        with ops.container("l1"):
            cnd_true = cond_v2.cond_v2(
                constant_op.constant(True), true_fn, false_fn)
            self.assertEqual(self.evaluate(cnd_true), 2)

            cnd_false = cond_v2.cond_v2(
                constant_op.constant(False), true_fn, false_fn)
            self.assertEqual(self.evaluate(cnd_false), 6)

            v4 = variables.Variable([3])
            q4 = data_flow_ops.FIFOQueue(1, dtypes.float32)
        v5 = variables.Variable([4])
        q5 = data_flow_ops.FIFOQueue(1, dtypes.float32)

    self.assertEqual(compat.as_bytes("l1"), container(v4))
    self.assertEqual(compat.as_bytes("l1"), container(q4.queue_ref))
    self.assertEqual(compat.as_bytes(""), container(v5))
    self.assertEqual(compat.as_bytes(""), container(q5.queue_ref))
