# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
if test.is_gpu_available(cuda_only=True):
    random_seed.set_random_seed(0)
    x = random_ops.truncated_normal([1, 784], seed=0)
    conv = _two_layer_model(x)
    dim = array_ops.placeholder(dtype='int32')
    split = array_ops.split(conv, 2, axis=dim)
    scale = constant_op.constant(0.1, shape=[32])
    offset = constant_op.constant(0.3, shape=[32])
    bn0 = nn.fused_batch_norm(split[0], scale, offset)
    bn1 = nn.fused_batch_norm(split[1], scale, offset)
    add = bn0[0] + bn1[0]
    output = array_ops.identity(add)

    with session.Session(config=_get_config(False)) as sess:
        output_val_ref = sess.run(output, feed_dict={dim: 3})

    with session.Session(config=_get_config()) as sess:
        metadata = config_pb2.RunMetadata()
        output_val = sess.run(output, run_metadata=metadata, feed_dict={dim: 3})

    nodes = []
    num_transposes = 0
    for node in metadata.cost_graph.node:
        if _is_transpose(node.name):
            num_transposes += 1
        nodes.append(node.name)

    expected_num_transposes = 2
    self.assertEqual(expected_num_transposes, num_transposes)
    self._assert_trans_nhwc_to_nchw('Conv2D-0', nodes)
    self._assert_trans_nchw_to_nhwc('add_2-0-0', nodes)
    self._assert_map_nhwc_to_nchw('split-0', nodes)
    self.assertAllClose(output_val_ref, output_val, atol=1e-3)
