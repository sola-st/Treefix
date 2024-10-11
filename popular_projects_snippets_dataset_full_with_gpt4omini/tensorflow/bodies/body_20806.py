# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
if test.is_gpu_available(cuda_only=True):
    random_seed.set_random_seed(0)
    x = random_ops.truncated_normal([1, 4, 2, 3, 3], seed=0)
    w = random_ops.truncated_normal([2, 2, 2, 3, 3], seed=0)
    conv3d = gen_nn_ops.conv3d(x, w, [1, 1, 1, 1, 1], 'SAME')
    y = math_ops.reduce_mean(conv3d, [0, 1, 2, 3], keepdims=True)
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

    # The reduce op Mean needs to dim map the input reduce index to NCDHW.
    # Then, the output needs to be tranposed back to NDHWC.
    expected_num_transposes = 2
    self.assertEqual(expected_num_transposes, num_transposes)
    self._assert_trans_ndhwc_to_ncdhw('Conv3D-0', nodes)
    self._assert_map_ndhwc_to_ncdhw('Mean-1', nodes)
    self._assert_trans_ncdhw_to_ndhwc('Mean-0-0', nodes)
    self.assertAllClose(output_val_ref, output_val, atol=1e-3)
