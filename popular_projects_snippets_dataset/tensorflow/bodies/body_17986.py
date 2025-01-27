# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
with backprop.GradientTape(persistent=True) as g:
    x = random_ops.random_uniform([3, 2, 12, 12, 3])
    g.watch(x)
    ksize = [1, 3, 3, 1]

def loop_fn(i):
    with g:
        x1 = array_ops.gather(x, i)
        output = nn.avg_pool(
            x1,
            ksize,
            strides=[1, 2, 2, 1],
            padding="VALID",
            data_format="NHWC")
        loss = nn.l2_loss(output)
    exit((output, g.gradient(loss, x1)))

self._test_loop_fn(loop_fn, 3)
