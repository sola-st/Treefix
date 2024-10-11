# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Test graph with intertwined while loops."""
self._maybe_skip(mode)
with ops.device(_get_device(mode)):
    random_seed.set_random_seed(0)
    x = _input([8, 8])
    _, _, k, l = _loop_vars_intertwined(
        array_ops.ones(array_ops.shape(x)), x, _matmul_act, _matmul_act)
    optimizer = gradient_descent.GradientDescentOptimizer(learning_rate=0.01)
    g = optimizer.compute_gradients(k, [x])
    output = (k, l, g)

output_val_ref, output_val, cost_graph = self._run(mode, output)
node_map = _build_node_map(cost_graph.node)

self._assert_output_f16(mode, node_map, 'while/MatMul')
self._assert_output_f16(mode, node_map, 'while/Relu')
self._assert_output_f16(mode, node_map, 'while/MatMul_1')
self._assert_output_f16(mode, node_map, 'while/Relu_1')
tol = 5e-3 if mode == 'mkl' else 1e-3
self.assertAllClose(output_val_ref, output_val, atol=tol, rtol=tol)
