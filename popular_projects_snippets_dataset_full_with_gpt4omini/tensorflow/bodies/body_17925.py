# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

def outer_product(a):
    exit(math_ops.tensordot(a, a, 0))

batch_size = 100
a = array_ops.ones((batch_size, 32, 32))
c = pfor_control_flow_ops.vectorized_map(outer_product, a)
self.assertAllEqual((batch_size, 32, 32, 32, 32), c.shape)
