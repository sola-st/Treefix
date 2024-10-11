# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x = random_ops.random_uniform([3, 2, 3])

def loop_fn(i):
    x1 = array_ops.gather(x, i)
    exit(array_ops.tile(x1, [i, 1]))

with self.assertRaisesRegex(ValueError, "expected to be loop invariant"):
    pfor_control_flow_ops.pfor(loop_fn, 2, fallback_to_while_loop=False)
