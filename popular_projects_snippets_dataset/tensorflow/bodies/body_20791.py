# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
if test.is_gpu_available(cuda_only=True):
    random_seed.set_random_seed(0)
    x = random_ops.truncated_normal([1, 784], seed=0)
    conv = _two_layer_model(x)
    axis = constant_op.constant(3)
    var = variables.Variable(3)
    assign = state_ops.assign(var, 6)
    with ops.control_dependencies([assign]):
        concat = array_ops.concat([conv, conv], axis)
    output = array_ops.identity(concat)

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

    # Four transposes were initially added in the Expand phase of
    # LayoutOptimizer; two of them are cancelled out in the Collapse phase.
    expected_num_transposes = 2
    self.assertEqual(expected_num_transposes, num_transposes)
    self._assert_trans_nhwc_to_nchw('Conv2D-0', nodes)
    self._assert_trans_nchw_to_nhwc('concat-0-0', nodes)
    self.assertIn('concat-2-LayoutOptimizer', nodes)
    self.assertAllClose(output_val_ref, output_val, atol=1e-3)
