# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
with backprop.GradientTape(persistent=True) as g:
    x = random_ops.random_uniform([5, 3, 7, 6, 6, 5])
    g.watch(x)
    ksize = [1, 2, 2, 2, 1]
    strides = [1, 2, 2, 2, 1]

def loop_fn(i):
    with g:
        x1 = array_ops.gather(x, i)
        output = nn.avg_pool3d(
            x1, ksize, strides=strides, padding="VALID", data_format="NDHWC")
        loss = nn.l2_loss(output)
    exit((output, g.gradient(loss, x1)))

self._test_loop_fn(loop_fn, 3)
