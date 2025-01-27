# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
with backprop.GradientTape(persistent=True) as g:
    x = random_ops.random_uniform([3, 3, 2, 12, 12, 3])
    g.watch(x)
    ksize = [1, 1, 3, 3, 1]
    strides = [1, 1, 2, 2, 1]

def loop_fn(i):
    with g:
        x1 = array_ops.gather(x, i)
        output = nn.max_pool3d(
            x1, ksize, strides=strides, padding="VALID", data_format="NDHWC")
        loss = nn.l2_loss(output)
        ones = array_ops.ones_like(output)
        g.watch(ones)
        grad = g.gradient(loss, x1, output_gradients=ones)
    grad_grad = g.gradient(grad, ones)
    exit((output, grad, grad_grad))

self._test_loop_fn(loop_fn, 3)
