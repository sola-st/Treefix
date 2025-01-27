# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
if test.is_gpu_available(cuda_only=True):
    random_seed.set_random_seed(0)
    x = random_ops.truncated_normal([4, 14, 14, 1], seed=0)
    w = random_ops.truncated_normal([2, 2, 1, 2], seed=0)
    y = nn.conv2d(x, w, strides=[1, 1, 1, 1], padding='SAME')
    y = nn.leaky_relu(y, alpha=0.2)
    output = array_ops.identity(y)

    with session.Session(config=_get_config(False)) as sess:
        output_val_ref = sess.run(output)

    with session.Session(config=_get_config()) as sess:
        metadata = config_pb2.RunMetadata()
        output_val = sess.run(output, run_metadata=metadata)

    nodes = []
    num_transposes = 0
    for node in metadata.cost_graph.node:
        if _is_transpose(node.name):
            num_transposes += 1
        nodes.append(node.name)

    expected_num_transposes = 2
    self.assertEqual(expected_num_transposes, num_transposes)
    self._assert_trans_nchw_to_nhwc('LeakyRelu-0-0', nodes)
    self.assertAllClose(output_val_ref, output_val, atol=1e-3)
