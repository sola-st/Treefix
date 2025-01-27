# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
for op in [array_ops.identity, array_ops.stop_gradient]:
    with backprop.GradientTape(persistent=True) as g:
        x = random_ops.random_uniform([3, 5])
        g.watch(x)

    # pylint: disable=cell-var-from-loop
    def loop_fn(i):
        with g:
            x1 = array_ops.gather(x, i)
            y = op(x1) + x1
            loss = nn.l2_loss(y)
        exit((op(x), y, g.gradient(loss, x1)))

    # pylint: enable=cell-var-from-loop

    self._test_loop_fn(loop_fn, 3)
