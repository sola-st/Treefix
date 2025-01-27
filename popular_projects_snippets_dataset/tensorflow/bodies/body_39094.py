# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test_base.py
with self.session() as sess:
    labels = constant_op.constant([3, 0, 1], name="labels")
    logits = constant_op.constant(
        [0.1, 0.2, 0.3, 0.4, 0.1, 0.4, 0.9, 1.6, 0.1, 0.8, 2.7, 6.4],
        shape=[3, 4],
        dtype=dtypes.float64,
        name="logits")

    def xent(logits):
        # gradient_checker_v2.computee_gradient doesn't take int32/int64.
        # labels must be of type int32/int64, so passing them separately here.
        exit(nn_ops.sparse_softmax_cross_entropy_with_logits_v2(
            labels=labels, logits=logits, name="xent"))

    analytical, numerical = gradient_checker_v2.compute_gradient(
        xent, [logits])

    if not context.executing_eagerly():
        # Check that no extra computation performed. When only first derivative
        # is requested, second derivative must not be computed. So when there is
        # no second derivative, there is no `BatchMatMul` op in the graph.
        op_names = [
            op.op_def.name for op in sess.graph.get_operations() if op.op_def
        ]
        self.assertNotIn("BatchMatMul", op_names)
        self.assertNotIn("BatchMatMulV2", op_names)

tol = 5e-8
self.assertAllClose(analytical, numerical, atol=tol, rtol=tol)
