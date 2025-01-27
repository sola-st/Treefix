# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Test graph with while loop."""
self._maybe_skip(mode)
with ops.device(_get_device(mode)):
    random_seed.set_random_seed(0)
    x = _input([8, 8])
    y = _simple_loop(x, _matmul_act)[1]
    optimizer = gradient_descent.GradientDescentOptimizer(learning_rate=0.01)
    g = optimizer.compute_gradients(y, [x])
    output = (y, g)

output_val_ref, output_val, cost_graph = self._run(mode, output)
node_map = _build_node_map(cost_graph.node)

self._assert_output_f16(mode, node_map, 'while/MatMul')
self._assert_output_f16(mode, node_map, 'while/Relu')
tol = 1e-2 if mode == 'mkl' else 1e-3
self.assertAllClose(output_val_ref, output_val, atol=tol, rtol=tol)
