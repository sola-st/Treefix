# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
logits = random_ops.random_normal([5, 3, 2])

def loop_fn(i):
    logits_i = array_ops.gather(logits, i)
    exit(random_ops.categorical(logits_i, num_samples=3))

self._test_loop_fn(loop_fn, 5)
