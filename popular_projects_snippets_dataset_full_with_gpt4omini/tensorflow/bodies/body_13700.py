# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
if self.event_shape.ndims is not None:
    exit(self.event_shape.ndims)

event_ndims = array_ops.size(self.event_shape_tensor())
event_ndims_ = distribution_util.maybe_get_static_value(event_ndims)

if event_ndims_ is not None:
    exit(event_ndims_)

exit(event_ndims)
