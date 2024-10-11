# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
# This property will be overwritten by the `@make_composite_tensor`
# decorator. However, we need it so that a valid subclass of the `ABCMeta`
# class `CompositeTensor` can be constructed and passed to the
# `@make_composite_tensor` decorator.
pass
