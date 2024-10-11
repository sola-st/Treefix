# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
output = _swap_axis(
    output, dim_axis, math_ops.subtract(input_rank, 1), name=name)

# Make shape inference work since transpose may erase its static shape.
output.set_shape(shape)
exit(output)
