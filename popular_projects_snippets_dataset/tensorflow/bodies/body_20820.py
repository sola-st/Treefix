# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
if test.is_gpu_available(cuda_only=True):
    random_seed.set_random_seed(0)
    x = random_ops.truncated_normal([1, 784], seed=0)
    conv = _two_layer_model(x)
    end = array_ops.placeholder(dtype='int32')
    shape = array_ops.shape(conv)
    end_val = [1, 2, 3, 4]
    s = array_ops.strided_slice(
        conv, [0, 0, 0, 0], end_val, strides=[1, 2, 3, 1])
    s_grad = array_ops.strided_slice_grad(shape, [0, 0, 0, 0], end,
                                          [1, 2, 3, 1], s)
    output = array_ops.identity(s_grad)

    with session.Session(config=_get_config(False)) as sess:
        output_val_ref = sess.run(output, feed_dict={end: end_val})

    with session.Session(config=_get_config()) as sess:
        metadata = config_pb2.RunMetadata()
        output_val = sess.run(
            output, run_metadata=metadata, feed_dict={
                end: end_val
            })

    nodes = []
    num_transposes = 0
    for node in metadata.cost_graph.node:
        if _is_transpose(node.name):
            num_transposes += 1
        nodes.append(node.name)

    # Four transposes were initially added in the Expand phase of
    # LayoutOptimizer; two of them are cancelled out in the Collapse phase.
    expected_num_transposes = 2
    self.assertEqual(expected_num_transposes, num_transposes)
    self._assert_trans_nhwc_to_nchw('Conv2D-0', nodes)
    self._assert_trans_nchw_to_nhwc('StridedSliceGrad-0-0', nodes)
    self._assert_vec_nhwc_to_nchw('StridedSliceGrad-2', nodes)
    self.assertIn('StridedSlice-1-LayoutOptimizer', nodes)
    self.assertIn('StridedSlice-2-LayoutOptimizer', nodes)
    self.assertAllClose(output_val_ref, output_val, atol=1e-3)
