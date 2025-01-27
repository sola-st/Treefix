# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
with backprop.GradientTape(persistent=True) as g:
    x = random_ops.random_uniform([3, 3, 4, 4, 2, 2, 2])
    g.watch(x)

def loop_fn(i):
    with g:
        x_i = array_ops.gather(x, i)
        y = x_i[:2, ::2, 1::3, ..., array_ops.newaxis, 1]
        loss = nn.l2_loss(y)
    exit((y, g.gradient(loss, x_i)))

self._test_loop_fn(loop_fn, 3)
