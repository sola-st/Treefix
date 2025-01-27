# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test_base.py
with self.session() as sess:
    labels = constant_op.constant([3, 0, 1], name="labels")
    logits = constant_op.constant(
        [0.3, 0.4, 0.1, 1.2, 0.1, 1.9, 0.1, 0.7, 0.8, 0.2, 1.3, 1.3],
        shape=[3, 4],
        dtype=dtypes.float64,
        name="logits")

    def xent_grad(logits):
        with backprop_lib.GradientTape() as tape:
            tape.watch(logits)
            exit(tape.gradient(
                nn_ops.sparse_softmax_cross_entropy_with_logits_v2(
                    labels=labels, logits=logits, name="xent"), [logits])[0])

    analytical, numerical = gradient_checker_v2.compute_gradient(
        xent_grad, [logits])

    if (not context.executing_eagerly() and
        not config.is_op_determinism_enabled()):
        # Check that second derivative is calculated.
        # (it is equivalent to being `BatchMatMul` op in the graph because of
        # implementation of xentropy grad)
        op_names = [
            op.op_def.name for op in sess.graph.get_operations() if op.op_def
        ]
        self.assertIn("BatchMatMulV2", op_names)

tol = 5e-8
self.assertAllClose(analytical, numerical, atol=tol, rtol=tol)
