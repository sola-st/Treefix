# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/optimize_for_inference_test.py
with self.cached_session() as sess:
    inputs = [1, 4, 2, 5, 3, 6, -1, -4, -2, -5, -3, -6]
    input_op = constant_op.constant(
        np.array(inputs), shape=[1, 2, 3, 2], dtype=dtypes.float32)
    resize_op = image_ops.resize_bilinear(
        input_op, [12, 4], align_corners=False)
    pad_op = array_ops.pad(resize_op, [[0, 0], [1, 1], [2, 2], [0, 0]],
                           mode="REFLECT")
    weights = [1, 2, 3, 4, 0.1, 0.2, 0.3, 0.4]
    weights_op = constant_op.constant(
        np.array(weights), shape=[1, 2, 2, 2], dtype=dtypes.float32)
    nn_ops.conv2d(
        pad_op, weights_op, [1, 1, 1, 1], padding="VALID", name="output")
    original_graph_def = sess.graph_def
    original_result = sess.run(["output:0"])
optimized_graph_def = optimize_for_inference_lib.fuse_resize_and_conv(
    original_graph_def, ["output"])

with self.cached_session() as sess:
    _ = importer.import_graph_def(
        optimized_graph_def, input_map={}, name="optimized")
    optimized_result = sess.run(["optimized/output:0"])

self.assertAllClose(original_result, optimized_result)

for node in optimized_graph_def.node:
    self.assertNotEqual("Conv2D", node.op)
    self.assertNotEqual("MirrorPad", node.op)
    self.assertNotEqual("ResizeBilinear", node.op)
