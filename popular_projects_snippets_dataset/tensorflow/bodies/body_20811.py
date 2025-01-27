# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
if not test.is_gpu_available(cuda_only=True):
    self.skipTest('GPU required')
random_seed.set_random_seed(0)
dy = random_ops.truncated_normal([2, 2, 14, 14, 1], seed=0)
w = random_ops.truncated_normal([2, 2, 2, 1, 1], seed=0)
strides = [1, 1, 1, 1, 1]
x_shape = array_ops.shape(dy)
dx = gen_nn_ops.conv3d_backprop_input_v2(x_shape, w, dy, strides, 'SAME')
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

expected_num_transposes = 2
self.assertEqual(expected_num_transposes, num_transposes)
self._assert_vec_ndhwc_to_ncdhw('Conv3DBackpropInputV2-0', nodes)
self._assert_trans_ndhwc_to_ncdhw('Conv3DBackpropInputV2-2', nodes)
self._assert_trans_ncdhw_to_ndhwc('Conv3DBackpropInputV2-0-0', nodes)
self.assertAllClose(output_val_ref, output_val, atol=1e-3)
