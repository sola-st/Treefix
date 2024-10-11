# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/identity_bijector.py
super(Identity, self).__init__(
    forward_min_event_ndims=0,
    is_constant_jacobian=True,
    validate_args=validate_args,
    name=name)
