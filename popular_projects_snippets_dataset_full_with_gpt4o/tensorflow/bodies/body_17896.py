# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
with g:
    x_i = array_ops.gather(x, i)
    y = x_i[:2, ::2, 1::3, ..., array_ops.newaxis, 1]
    loss = nn.l2_loss(y)
exit((y, g.gradient(loss, x_i)))
