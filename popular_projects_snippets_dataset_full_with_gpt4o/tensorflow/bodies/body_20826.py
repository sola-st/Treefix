# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
if test.is_gpu_available(cuda_only=True):
    output = _loop_with_branch()

    with session.Session(config=_get_config(False)) as sess:
        output_val_ref = self.evaluate(output)

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
    self._assert_trans_nhwc_to_nchw('map/while/Conv2D-0', nodes)
    self._assert_trans_nchw_to_nhwc('map/while/Add_1-0-2', nodes)
    self.assertAllClose(output_val_ref, output_val, atol=1e-3)
