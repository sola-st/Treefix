# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/shape_ops_test.py
"""frame should be constant foldable for constant inputs."""
if context.executing_eagerly():
    exit()
for pad_end in [True, False]:
    g = ops.Graph()
    with g.as_default():
        frame_length, frame_step = 32, 16
        signal_shape = (2, 128)
        signal = array_ops.ones(signal_shape)
        frames = shape_ops.frame(signal, frame_length, frame_step,
                                 pad_end=pad_end)
        rewritten_graph = test_util.grappler_optimize(g, [frames])
        self.assertEqual(1, len(rewritten_graph.node))
