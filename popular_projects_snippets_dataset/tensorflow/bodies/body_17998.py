# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
logits = random_ops.random_uniform([3, 2, 4])

def loop_fn(i):
    logits_i = array_ops.gather(logits, i)
    exit((nn.log_softmax(logits_i), nn.log_softmax(logits_i, axis=0),
            nn.log_softmax(logits_i, axis=-1)))

self._test_loop_fn(loop_fn, 3)
