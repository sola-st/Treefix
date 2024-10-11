# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Test graph with recurrent lstm."""
self._maybe_skip(mode)
with ops.device(_get_device(mode)):
    random_seed.set_random_seed(0)
    init_c = _input([8, 4])
    init_h = _input([8, 4])
    _, _, h, _ = _recurrent_lstm(init_c, init_h)
    optimizer = gradient_descent.GradientDescentOptimizer(learning_rate=0.01)
    g = optimizer.compute_gradients(h, [init_c, init_h])
    output = (h, g)

output_val_ref, output_val, cost_graph = self._run(mode, output)
node_map = _build_node_map(cost_graph.node)

self._assert_output_f16(mode, node_map, 'while/concat')
self._assert_output_f16(mode, node_map, 'while/MatMul')
self._assert_output_f16(mode, node_map, 'while/split')
self._assert_output_f16(mode, node_map, 'while/Sigmoid')
self._assert_output_f16(mode, node_map, 'while/Sigmoid_1')
self._assert_output_f16(mode, node_map, 'while/Sigmoid_2')
self._assert_output_f16(mode, node_map, 'while/Tanh')
self._assert_output_f16(mode, node_map, 'while/Tanh_1')
self.assertAllClose(output_val_ref, output_val, atol=1e-3, rtol=1e-3)
