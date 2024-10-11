# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
with g:
    x1 = array_ops.gather(x, i)
    y = op(x1) + x1
    loss = nn.l2_loss(y)
exit((op(x), y, g.gradient(loss, x1)))
