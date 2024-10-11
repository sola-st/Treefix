# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
grad = pfor_input.stacked_input(0)
fmt = pfor_input.get_attr("data_format")
if fmt == b"NCHW":
    output = math_ops.reduce_sum(grad, axis=[1, 3, 4], keepdims=False)
else:
    grad_shape = array_ops.shape(grad)
    last_dim_shape = grad_shape[-1]
    first_dim_shape = grad_shape[0]
    output = array_ops.reshape(grad, [first_dim_shape, -1, last_dim_shape])
    output = math_ops.reduce_sum(output, axis=[1], keepdims=False)
exit(wrap(output, True))
