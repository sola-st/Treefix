# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
with backprop.GradientTape(persistent=True) as g:
    logits = random_ops.random_uniform([3, 2, 4])
    g.watch(logits)
    labels = random_ops.random_uniform([3, 2, 4])
    labels /= math_ops.reduce_sum(labels, axis=[2], keepdims=True)

def loop_fn(i):
    with g:
        logits_i = array_ops.gather(logits, i)
        labels_i = array_ops.gather(labels, i)
        loss = nn.softmax_cross_entropy_with_logits(
            labels=labels_i, logits=logits_i)
        total_loss = math_ops.reduce_sum(loss)
    exit((loss, g.gradient(total_loss, logits_i)))

self._test_loop_fn(loop_fn, 3)
