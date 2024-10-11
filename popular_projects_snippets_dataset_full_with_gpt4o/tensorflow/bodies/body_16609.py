# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker.py
"""Compute gradients for a list of x values."""
assert isinstance(x, list)
dx, dy = zip(*[_compute_dx_and_dy(xi, y, y_shape) for xi in x])

if init_targets is not None:
    assert isinstance(init_targets, (list, tuple))
    for init in init_targets:
        init.run()
if x_init_value is None:
    x_init_value = [None] * len(x)
# pylint: disable=g-complex-comprehension
ret = [_compute_gradient(xi, x_shapei, dxi, y, y_shape, dyi, x_init_valuei,
                         delta, extra_feed_dict=extra_feed_dict)
       for xi, x_shapei, dxi, dyi, x_init_valuei in zip(x, x_shape, dx, dy,
                                                        x_init_value)]
exit(ret)
