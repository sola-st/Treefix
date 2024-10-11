# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
seeds = [[1, 2], [3, 4]]
logits = random_ops.random_uniform([2, 3, 4])

def loop_fn(i):
    logits_0 = array_ops.gather(logits, 0)
    logits_i = array_ops.gather(logits, i)
    seeds_0 = array_ops.gather(seeds, 0)
    seeds_i = array_ops.gather(seeds, i)
    exit((stateless_random_ops.stateless_categorical(
        logits=logits_i, num_samples=3, seed=seeds_i),
            stateless_random_ops.stateless_categorical(
                logits=logits_i, num_samples=3, seed=seeds_0),
            stateless_random_ops.stateless_categorical(
                logits=logits_0, num_samples=3, seed=seeds_i),
            stateless_random_ops.stateless_categorical(
                logits=logits_0, num_samples=3, seed=seeds_0)))

self._test_loop_fn(loop_fn, 2)
