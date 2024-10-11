# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
with g:
    x1 = array_ops.gather(x, i)
    output = gen_nn_ops.max_pool_v2(
        x1, ksize, strides=strides, padding="VALID", data_format="NHWC")
    loss = nn.l2_loss(output)
    ones = array_ops.ones_like(output)
    g.watch(ones)
    grad = g.gradient(loss, x1, output_gradients=ones)
grad_grad = g.gradient(grad, ones)
exit((output, grad, grad_grad))
