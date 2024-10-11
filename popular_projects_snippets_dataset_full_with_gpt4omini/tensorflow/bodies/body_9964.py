# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/optimize_for_inference_test.py
for data_format, conv2d_func in [("NHWC", nn_ops.conv2d),
                                 ("NCHW", nn_ops.conv2d),
                                 ("NHWC", nn_ops.depthwise_conv2d_native),
                                 ("NCHW", nn_ops.depthwise_conv2d_native)]:
    with self.cached_session() as sess:
        inputs = [1, 4, 2, 5, 3, 6, -1, -4, -2, -5, -3, -6]
        input_op = constant_op.constant(
            np.array(inputs),
            shape=[1, 1, 6, 2] if data_format == "NHWC" else [1, 2, 1, 6],
            dtype=dtypes.float32)
        if conv2d_func == nn_ops.conv2d:
            weights = [1, 2, 3, 4, 0.1, 0.2, 0.3, 0.4]
            weights_op = constant_op.constant(
                np.array(weights), shape=[1, 2, 2, 2], dtype=dtypes.float32)
        else:
            weights = [1, 2, 0.3, 0.4]
            weights_op = constant_op.constant(
                np.array(weights), shape=[1, 2, 2, 1], dtype=dtypes.float32)
        mean_op = constant_op.constant(
            np.array([10, 20]), shape=[2], dtype=dtypes.float32)
        variance_op = constant_op.constant(
            np.array([0.25, 0.5]), shape=[2], dtype=dtypes.float32)
        beta_op = constant_op.constant(
            np.array([0.1, 0.6]), shape=[2], dtype=dtypes.float32)
        gamma_op = constant_op.constant(
            np.array([1.0, 2.0]), shape=[2], dtype=dtypes.float32)
        ops.get_default_graph().graph_def_versions.producer = 9
        conv_op = conv2d_func(
            input_op,
            weights_op, [1, 1, 1, 1],
            padding="SAME",
            data_format=data_format,
            name="conv_op")
        gen_nn_ops.fused_batch_norm_v3(
            conv_op,
            gamma_op,
            beta_op,
            mean_op,
            variance_op,
            0.00001,
            is_training=False,
            data_format=data_format,
            name="output")
        original_graph_def = sess.graph_def
        original_result = sess.run(["output:0"])
    optimized_graph_def = optimize_for_inference_lib.fold_batch_norms(
        original_graph_def)
with self.cached_session() as sess:
    _ = importer.import_graph_def(
        optimized_graph_def, input_map={}, name="optimized")
    optimized_result = sess.run(["optimized/output:0"])

    self.assertAllClose(
        original_result, optimized_result, rtol=1e-04, atol=1e-06)

    for node in optimized_graph_def.node:
        self.assertNotEqual("FusedBatchNormV3", node.op)
