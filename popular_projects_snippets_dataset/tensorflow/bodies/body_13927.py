# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
"""Helper to `sample`; sets static shape info."""
# Set shape hints.
sample_shape = tensor_shape.TensorShape(
    tensor_util.constant_value(sample_shape))

ndims = x.get_shape().ndims
sample_ndims = sample_shape.ndims
batch_ndims = self.batch_shape.ndims
event_ndims = self.event_shape.ndims

# Infer rank(x).
if (ndims is None and
    sample_ndims is not None and
    batch_ndims is not None and
    event_ndims is not None):
    ndims = sample_ndims + batch_ndims + event_ndims
    x.set_shape([None] * ndims)

# Infer sample shape.
if ndims is not None and sample_ndims is not None:
    shape = sample_shape.concatenate([None]*(ndims - sample_ndims))
    x.set_shape(x.get_shape().merge_with(shape))

# Infer event shape.
if ndims is not None and event_ndims is not None:
    shape = tensor_shape.TensorShape(
        [None]*(ndims - event_ndims)).concatenate(self.event_shape)
    x.set_shape(x.get_shape().merge_with(shape))

# Infer batch shape.
if batch_ndims is not None:
    if ndims is not None:
        if sample_ndims is None and event_ndims is not None:
            sample_ndims = ndims - batch_ndims - event_ndims
        elif event_ndims is None and sample_ndims is not None:
            event_ndims = ndims - batch_ndims - sample_ndims
    if sample_ndims is not None and event_ndims is not None:
        shape = tensor_shape.TensorShape([None]*sample_ndims).concatenate(
            self.batch_shape).concatenate([None]*event_ndims)
        x.set_shape(x.get_shape().merge_with(shape))

exit(x)
