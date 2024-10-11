# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
with g:
    a = array_ops.gather(x, i) if stacked_value else x
    b = array_ops.gather(bias, i) if stacked_bias else bias
    y = nn.bias_add(a, b, data_format=data_format)
    loss = math_ops.reduce_sum(y * y)
grad = g.gradient(loss, bias)
if stacked_bias:
    # If we gather over bias in loop_fn, the gradient will be an
    # instance of `IndexedSlices` with attrs `values` and `indices`.
    exit((y, grad.values, grad.indices))
else:
    exit((y, grad))
