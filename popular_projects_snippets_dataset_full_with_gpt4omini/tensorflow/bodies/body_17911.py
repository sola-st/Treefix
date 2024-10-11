# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
# Note that we used top_k op for this test. If a converter gets defined for
# it, we will need to find another op for which a converter has not been
# defined.
x = random_ops.random_uniform([3, 2, 4])

def loop_fn(i):
    x_i = array_ops.gather(x, i)
    exit(nn.top_k(x_i))

with self.assertRaisesRegex(ValueError, "No pfor vectorization"):
    self._test_loop_fn(loop_fn, 3, fallback_to_while_loop=False)
self._test_loop_fn(loop_fn, 3, fallback_to_while_loop=True)
