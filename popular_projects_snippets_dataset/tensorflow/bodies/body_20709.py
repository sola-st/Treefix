# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Test graph with convolution followed by batch norm."""
self._maybe_skip(mode)
if mode == 'cuda':
    # TODO(reedwm): enable these tests when cuDNN is upgraded to >= 7.6.2.
    self.skipTest('Test case should be skipped when cuDNN < 7.6.2')
with ops.device(_get_device(mode)):
    random_seed.set_random_seed(0)
    x = _input([2, 8, 8, 8, 1])
    x = _conv3d_bn(x)
    output = _conv3d_bn(x)

output_val_ref, output_val, cost_graph = self._run(mode, output)
node_map = _build_node_map(cost_graph.node)
num_to_fp16, num_to_fp32 = _count_casts(mode, cost_graph.node)

self._assert_output_f16(mode, node_map, 'Conv3D')
self._assert_output_f16(mode, node_map, 'FusedBatchNormV3')
self._assert_output_f16(mode, node_map, 'Conv3D_1')
self.assertEqual(num_to_fp16, 3)  # Before Conv3D:0, Conv3D:1, Conv3D_1:1
self.assertEqual(num_to_fp32, 1)  # After FusedBatchNormV3:0
self.assertAllClose(output_val_ref, output_val, atol=1e-2, rtol=1e-2)
