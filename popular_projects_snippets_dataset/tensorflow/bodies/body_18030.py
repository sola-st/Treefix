# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x = random_ops.random_uniform([3, 5])

def loop_fn(i):
    x1 = array_ops.gather(x, i)
    exit(logging_ops.Print(
        x1, [x1, "x1", array_ops.shape(x1)], summarize=10))

self._test_loop_fn(loop_fn, 3)
