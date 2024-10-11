# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
if test.is_gpu_available(cuda_only=True):
    random_seed.set_random_seed(0)
    x = random_ops.truncated_normal([1, 4, 2, 3, 3], seed=0)
    w = random_ops.truncated_normal([2, 2, 2, 3, 3], seed=0)
    mean = random_ops.truncated_normal([1, 1, 1, 1, 3], seed=0)
    variance = random_ops.truncated_normal([1, 1, 1, 1, 3], seed=0)
    gamma = random_ops.truncated_normal([1, 1, 1, 1, 3], seed=0)
    beta = random_ops.truncated_normal([1, 1, 1, 1, 3], seed=0)
    conv3d = gen_nn_ops.conv3d(x, w, [1, 1, 1, 1, 1], 'SAME')
    y = nn.batch_normalization(
        conv3d,
        mean=mean,
        variance=variance,
        scale=gamma,
        offset=beta,
        variance_epsilon=0.001)
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

    # The binary ops mul_1 and add_1 in batch norm need to transpose one of
    # the two inputs to NCDHW. The other input has already been tranposed via
    # Conv3D.
    expected_num_transposes = 4
    self.assertEqual(expected_num_transposes, num_transposes)
    self._assert_trans_ndhwc_to_ncdhw('Conv3D-0', nodes)
    self._assert_trans_ndhwc_to_ncdhw('batchnorm/mul_1-1', nodes)
    self._assert_trans_ndhwc_to_ncdhw('batchnorm/add_1-1', nodes)
    self._assert_trans_ncdhw_to_ndhwc('batchnorm/add_1-0-0', nodes)
