# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_test_base.py
with self.cached_session() as sess:
    labels = constant_op.constant([
        0.0, 0.0, 1.0 / 3, 0.0, 1.0 / 3, 0.0, 0.0, 0.0, 0.0, 0.5 / 3, 0.0,
        0.5 / 3
    ],
                                  shape=[12],
                                  dtype=dtypes.float64,
                                  name="labels")
    logits = constant_op.constant(
        [0.1, 0.2, 0.3, 0.4, 0.1, 0.4, 0.9, 1.6, 0.1, 0.8, 2.7, 6.4],
        shape=[12],
        dtype=dtypes.float64,
        name="logits")
    x = nn_ops.softmax_cross_entropy_with_logits(
        labels=labels, logits=logits, name="xent")
    loss = math_ops.reduce_sum(x)

    gradients = gradients_impl.gradients(loss, [logits])[0]

    err = gradient_checker.compute_gradient_error(logits, [12], gradients,
                                                  [12])

    if not config.is_op_determinism_enabled():
        # Check how second derivative is calculated.
        # (it is equivalent to a `BatchMatMul` op being in the graph because of
        # the implementation in SoftmaxCrossEntropyWithLogitsGrad)
        op_names = [
            op.op_def.name for op in sess.graph.get_operations() if op.op_def
        ]
        self.assertIn("BatchMatMulV2", op_names)

self.assertLess(err, 5e-8)
