# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/optimize_for_inference_test.py
with self.cached_session() as sess:
    inputs = [1, 4, 2, 5, 3, 6, -1, -4, -2, -5, -3, -6]
    input_op = constant_op.constant(
        np.array(inputs), shape=[1, 1, 6, 2], dtype=dtypes.float32)
    weights = [1, 2, 3, 4, 0.1, 0.2, 0.3, 0.4]
    weights_op = constant_op.constant(
        np.array(weights), shape=[1, 2, 2, 2], dtype=dtypes.float32)
    conv_op = nn_ops.conv2d(
        input_op, weights_op, [1, 1, 1, 1], padding="SAME", name="conv_op")
    mean_op = constant_op.constant(
        np.array([10, 20]), shape=[2], dtype=dtypes.float32)
    variance_op = constant_op.constant(
        np.array([0.25, 0.5]), shape=[2], dtype=dtypes.float32)
    beta_op = constant_op.constant(
        np.array([0.1, 0.6]), shape=[2], dtype=dtypes.float32)
    gamma_op = constant_op.constant(
        np.array([1.0, 2.0]), shape=[2], dtype=dtypes.float32)
    test_util.set_producer_version(ops.get_default_graph(), 8)
    gen_nn_ops._batch_norm_with_global_normalization(
        conv_op,
        mean_op,
        variance_op,
        beta_op,
        gamma_op,
        0.00001,
        False,
        name="output")
    original_graph_def = sess.graph_def
    original_result = sess.run(["output:0"])
optimized_graph_def = optimize_for_inference_lib.fold_batch_norms(
    original_graph_def)

with self.cached_session() as sess:
    _ = importer.import_graph_def(
        optimized_graph_def, input_map={}, name="optimized")
    optimized_result = sess.run(["optimized/output:0"])

self.assertAllClose(original_result, optimized_result)

for node in optimized_graph_def.node:
    self.assertNotEqual("BatchNormWithGlobalNormalization", node.op)
