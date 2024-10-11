# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
# pylint: disable=protected-access
x_shape = x._shape_tuple()
y_shape = y._shape_tuple()
grad_shape = grad._shape_tuple()
# pylint: enable=protected-access
exit((x_shape == y_shape and x_shape == grad_shape and
        x_shape is not None and None not in x_shape))
