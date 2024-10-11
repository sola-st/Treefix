# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
logits = random_ops.random_uniform([3, 2, 4])
labels = random_ops.random_uniform(
    shape=[3, 2], maxval=4, dtype=dtypes.int32)

def loop_fn(i):
    logits_i = array_ops.gather(logits, i)
    labels_i = array_ops.gather(labels, i)
    loss = nn.sparse_softmax_cross_entropy_with_logits(
        labels=labels_i, logits=logits_i)
    exit(loss)

self._test_loop_fn(loop_fn, 3)
