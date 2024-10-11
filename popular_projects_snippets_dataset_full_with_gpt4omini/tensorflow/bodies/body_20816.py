# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
if not test.is_gpu_available(cuda_only=True):
    self.skipTest('GPU required')
random_seed.set_random_seed(0)
x = random_ops.truncated_normal([2, 2, 14, 14, 1], seed=0)
w = random_ops.truncated_normal([2, 2, 2, 1, 2], seed=0)
strides = [1, 1, 1, 1, 1]
y = gen_nn_ops.conv3d(x, w, strides, 'SAME')
size = array_ops.placeholder(dtype='int32')
s = array_ops.slice(y, [0, 0, 0, 0, 0], size)
output = array_ops.identity(s)

size_val = [1, 1, 2, 2, 1]
with session.Session(config=_get_config(False)) as sess:
    output_val_ref = sess.run(output, feed_dict={size: size_val})

with session.Session(config=_get_config()) as sess:
    metadata = config_pb2.RunMetadata()
    output_val = sess.run(
        output, run_metadata=metadata, feed_dict={size: size_val})

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
self._assert_trans_ndhwc_to_ncdhw('Conv3D-0', nodes)
self._assert_trans_ncdhw_to_ndhwc('Slice-0-0', nodes)
self._assert_vec_ndhwc_to_ncdhw('Slice-2', nodes)
self.assertAllClose(output_val_ref, output_val, atol=1e-3)
