# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Test graph with convolution followed by pooling."""
self._maybe_skip(mode)
with ops.device(_get_device(mode)):
    random_seed.set_random_seed(0)
    x = _input([2, 8, 8, 1])
    output = _conv_pool(x)

output_val_ref, output_val, cost_graph = self._run(mode, output)
node_map = _build_node_map(cost_graph.node)
num_to_f16, num_to_fp32 = _count_casts(mode, cost_graph.node)

self._assert_output_f16(mode, node_map, 'Conv2D')
self._assert_output_f16(mode, node_map, 'Relu')
self._assert_output_f16(mode, node_map, 'MaxPool')
self._assert_output_f16(mode, node_map, 'Conv2D_1')
self.assertEqual(num_to_f16, 4)
self.assertEqual(num_to_fp32, 1)
tol = 5e-3 if mode == 'mkl' else 1e-3
self.assertAllClose(output_val_ref, output_val, atol=tol, rtol=tol)
