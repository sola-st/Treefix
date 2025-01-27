# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
if test.is_gpu_available(cuda_only=True):
    random_seed.set_random_seed(0)
    x = random_ops.truncated_normal([1, 784], seed=0)
    conv = _two_layer_model(x)
    ksize = constant_op.constant([1, 2, 3, 1], shape=[4])
    strides = array_ops.placeholder(dtype='int32', shape=[4])
    max_pool = gen_nn_ops.max_pool_v2(conv, ksize, strides, 'VALID')
    output = array_ops.identity(max_pool)

    strides_val = [1, 3, 2, 1]
    with session.Session(config=_get_config(False)) as sess:
        output_val_ref = sess.run(output, feed_dict={strides: strides_val})

    with session.Session(config=_get_config()) as sess:
        metadata = config_pb2.RunMetadata()
        output_val = sess.run(
            output, run_metadata=metadata, feed_dict={
                strides: strides_val
            })

    nodes = []
    num_transposes = 0
    for node in metadata.cost_graph.node:
        if _is_transpose(node.name):
            num_transposes += 1
        nodes.append(node.name)

    expected_num_transposes = 2
    self.assertEqual(expected_num_transposes, num_transposes)
    self._assert_trans_nhwc_to_nchw('Conv2D-0', nodes)
    self._assert_trans_nchw_to_nhwc('MaxPoolV2-0-0', nodes)
    self._assert_vec_nhwc_to_nchw('MaxPoolV2-2', nodes)
    self.assertIn('MaxPoolV2-1-LayoutOptimizer', nodes)
    self.assertAllClose(output_val_ref, output_val, atol=1e-3)
