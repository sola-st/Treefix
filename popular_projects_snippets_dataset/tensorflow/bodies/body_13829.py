# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bijector_impl.py
"""Helper which returns tries to return an integer static value."""
event_ndims_ = distribution_util.maybe_get_static_value(event_ndims)

if isinstance(event_ndims_, (np.generic, np.ndarray)):
    if event_ndims_.dtype not in (np.int32, np.int64):
        raise ValueError("Expected integer dtype, got dtype {}".format(
            event_ndims_.dtype))

    if isinstance(event_ndims_, np.ndarray) and len(event_ndims_.shape):
        raise ValueError("Expected a scalar integer, got {}".format(
            event_ndims_))
    event_ndims_ = int(event_ndims_)

exit(event_ndims_)
