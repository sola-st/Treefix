# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
if test.is_gpu_available(cuda_only=True):
    x = array_ops.placeholder(dtype='float32')
    conv = _two_layer_model(x)
    shapen = array_ops.shape_n([conv, conv])
    output = math_ops.add(shapen[0], shapen[1])

    x_val = [1.7] * 784
    with session.Session(config=_get_config(False)) as sess:
        output_val_ref = sess.run(output, feed_dict={x: x_val})

    with session.Session(config=_get_config()) as sess:
        metadata = config_pb2.RunMetadata()
        output_val = sess.run(
            output, run_metadata=metadata, feed_dict={
                x: x_val
            })

    nodes = []
    num_transposes = 0
    for node in metadata.cost_graph.node:
        if _is_transpose(node.name):
            num_transposes += 1
        nodes.append(node.name)

    expected_num_transposes = 1
    self.assertEqual(expected_num_transposes, num_transposes)
    self._assert_trans_nhwc_to_nchw('Conv2D-0', nodes)
    self._assert_vec_nchw_to_nhwc('ShapeN-0-0', nodes)
    self.assertAllEqual(output_val_ref, output_val)
