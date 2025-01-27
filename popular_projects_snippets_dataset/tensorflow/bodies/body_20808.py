# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
if test.is_gpu_available(cuda_only=True):
    random_seed.set_random_seed(0)
    x_3d = random_ops.truncated_normal([1, 4, 2, 3, 3], seed=0)
    filters = random_ops.truncated_normal([2, 2, 2, 3, 3], seed=0)
    strides_val = [1, 1, 1, 1, 1]
    scale = constant_op.constant(0.1, shape=[3])
    offset = constant_op.constant(0.3, shape=[3])
    conv3d = gen_nn_ops.conv3d(x_3d, filters, strides_val, 'SAME')
    y, _, _ = nn.fused_batch_norm(conv3d, scale, offset, data_format='NDHWC')
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
    self._assert_trans_ndhwc_to_ncdhw('Conv3D-0', nodes)
    self._assert_trans_ncdhw_to_ndhwc('FusedBatchNormV3-0-0', nodes)
    self.assertAllClose(output_val_ref, output_val, atol=1e-3)
