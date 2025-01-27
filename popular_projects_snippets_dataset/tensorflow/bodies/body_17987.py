# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
with g:
    x1 = array_ops.gather(x, i)
    output = nn.avg_pool3d(
        x1, ksize, strides=strides, padding="VALID", data_format="NDHWC")
    loss = nn.l2_loss(output)
exit((output, g.gradient(loss, x1)))
