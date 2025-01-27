# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
if test.is_gpu_available(cuda_only=True):
    random_seed.set_random_seed(0)
    x = random_ops.truncated_normal([1, 784], seed=0)
    conv = _two_layer_model(x)
    add = math_ops.add(conv, conv)
    condition = array_ops.placeholder(dtype='bool')
    select = gen_math_ops.select(condition, conv, add)
    output = array_ops.identity(select)

    condition_val = np.zeros((1, 7, 7, 64))
    with session.Session(config=_get_config(False)) as sess:
        output_val_ref = sess.run(output, feed_dict={condition: condition_val})

    with session.Session(config=_get_config()) as sess:
        metadata = config_pb2.RunMetadata()
        output_val = sess.run(
            output, run_metadata=metadata, feed_dict={condition: condition_val})

    nodes = []
    num_transposes = 0
    for node in metadata.cost_graph.node:
        if _is_transpose(node.name):
            num_transposes += 1
        nodes.append(node.name)

    expected_num_transposes = 3
    self.assertEqual(expected_num_transposes, num_transposes)
    self._assert_trans_nhwc_to_nchw('Conv2D-0', nodes)
    self.assertAllClose(output_val_ref, output_val, atol=1e-3)
