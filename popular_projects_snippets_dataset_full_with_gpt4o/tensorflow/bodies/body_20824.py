# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
if test.is_gpu_available(cuda_only=True):
    x = array_ops.placeholder(dtype='float32')
    conv = _two_layer_model(x)
    conv_reshape = array_ops.reshape(conv, [1, 1, 1, -1])
    shapen = array_ops.shape_n([conv, conv_reshape])
    shape = array_ops.identity(shapen[1])
    ones = array_ops.ones(shape)
    output = math_ops.add_n([conv_reshape, ones])

    x_val = [1.7] * 784
    with session.Session(config=_get_config(False)) as sess:
        output_val_ref = sess.run(output, feed_dict={x: x_val})

    with session.Session(config=_get_config()) as sess:
        metadata = config_pb2.RunMetadata()
        output_val = sess.run(
            output, run_metadata=metadata, feed_dict={x: x_val})

    nodes = []
    num_transposes = 0
    for node in metadata.cost_graph.node:
        if _is_transpose(node.name):
            num_transposes += 1
        nodes.append(node.name)

    expected_num_transposes = 2
    self.assertEqual(expected_num_transposes, num_transposes)
    self._assert_trans_nhwc_to_nchw('Conv2D-0', nodes)
    self.assertAllClose(output_val_ref, output_val, atol=1e-3)
