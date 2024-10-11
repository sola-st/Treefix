# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
if not test.is_gpu_available(cuda_only=True):
    self.skipTest('GPU required')
h = array_ops.placeholder(dtype='float32')
x = array_ops.reshape(h, [-1, 2, 14, 14, 1])
w = random_ops.truncated_normal([2, 2, 2, 1, 4], seed=0)
strides = [1, 1, 1, 1, 1]
y = gen_nn_ops.conv3d(x, w, strides, 'SAME')
x1 = array_ops.reshape(h, [-1, 784])
y1 = _two_layer_model(x1)
outputs = array_ops.identity_n([y1, y])
new_x0 = array_ops.reshape(outputs[0], [-1, 2, 14, 14, 1])
new_x1 = array_ops.reshape(outputs[1], [-1, 2, 14, 14, 1])
output = math_ops.add(new_x0, new_x1)

x_val = [1.7] * 784
with session.Session(config=_get_config(False)) as sess:
    output_val_ref = sess.run(output, feed_dict={h: x_val})

with session.Session(config=_get_config()) as sess:
    metadata = config_pb2.RunMetadata()
    output_val = sess.run(output, run_metadata=metadata, feed_dict={h: x_val})

nodes = []
num_transposes = 0
for node in metadata.cost_graph.node:
    if _is_transpose(node.name):
        num_transposes += 1
    nodes.append(node.name)

expected_num_transposes = 4
self.assertEqual(expected_num_transposes, num_transposes)
self._assert_trans_ndhwc_to_ncdhw('Conv3D-0', nodes)
self._assert_trans_nhwc_to_nchw('Conv2D-0', nodes)
self._assert_trans_ncdhw_to_ndhwc('IdentityN-1-0', nodes)
self._assert_trans_nchw_to_nhwc('IdentityN-0-0', nodes)
self.assertAllClose(output_val_ref, output_val, atol=1e-3)
