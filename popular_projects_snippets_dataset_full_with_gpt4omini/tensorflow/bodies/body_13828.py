# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bijector_impl.py
"""Check whether event_ndims is at least min_event_ndims."""
event_ndims = ops.convert_to_tensor(event_ndims, name="event_ndims")
event_ndims_ = tensor_util.constant_value(event_ndims)
assertions = []

if not event_ndims.dtype.is_integer:
    raise ValueError("Expected integer dtype, got dtype {}".format(
        event_ndims.dtype))

if event_ndims_ is not None:
    if event_ndims.shape.ndims != 0:
        raise ValueError("Expected scalar event_ndims, got shape {}".format(
            event_ndims.shape))
    if min_event_ndims > event_ndims_:
        raise ValueError("event_ndims ({}) must be larger than "
                         "min_event_ndims ({})".format(
                             event_ndims_, min_event_ndims))
elif self.validate_args:
    assertions += [
        check_ops.assert_greater_equal(event_ndims, min_event_ndims)]

if event_ndims.shape.is_fully_defined():
    if event_ndims.shape.ndims != 0:
        raise ValueError("Expected scalar shape, got ndims {}".format(
            event_ndims.shape.ndims))

elif self.validate_args:
    assertions += [
        check_ops.assert_rank(event_ndims, 0, message="Expected scalar.")]
exit(assertions)
