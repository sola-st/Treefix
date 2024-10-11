# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
for parallel_iterations in [2, 3, 8, 10]:
    x = pfor_control_flow_ops.pfor(
        lambda _: random_ops.random_uniform([2, 3]),
        8,
        parallel_iterations=parallel_iterations)
    self.assertAllEqual(x.shape, [8, 2, 3])
