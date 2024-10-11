# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
if test.is_gpu_available(cuda_only=True):
    random_seed.set_random_seed(0)
    x_3d = random_ops.truncated_normal([1, 4, 2, 3, 3], seed=0)
    filters = random_ops.truncated_normal([2, 2, 2, 3, 3], seed=0)
    strides_val = [1, 1, 1, 1, 1]
    scale = constant_op.constant(0.1, shape=[3])
    offset = constant_op.constant(0.3, shape=[3])
    mean = constant_op.constant(0.1, shape=[3])
    variance = constant_op.constant(0.3, shape=[3])
    conv3d = gen_nn_ops.conv3d(x_3d, filters, strides_val, 'SAME')
    y, running_mean, running_var, r0, r1, r2 = gen_nn_ops.fused_batch_norm_v3(
        conv3d,
        scale,
        offset,
        mean,
        variance,
        epsilon=1.001e-5,
        exponential_avg_factor=1.0,
        data_format='NDHWC',
        is_training=True,
        name='batch_norm')
    dx, dscale, doffset, _, _ = gen_nn_ops.fused_batch_norm_grad_v3(
        y,
        x_3d,
        scale,
        r0,
        r1,
        r2,
        epsilon=1.001e-5,
        data_format='NDHWC',
        is_training=True)
    output = array_ops.identity(dx)

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

    expected_num_transposes = 3
    self.assertEqual(expected_num_transposes, num_transposes)
    self._assert_trans_ndhwc_to_ncdhw('Conv3D-0', nodes)
    self._assert_trans_ndhwc_to_ncdhw('FusedBatchNormGradV3-1', nodes)
    self._assert_trans_ncdhw_to_ndhwc('FusedBatchNormGradV3-0-0', nodes)
    self.assertAllClose(output_val_ref, output_val, atol=1e-3)
