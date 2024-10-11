# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
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
