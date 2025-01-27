# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
if (
    isinstance(other, Index)
    and is_object_dtype(other.dtype)
    and type(other) is not Index
):
    # We return NotImplemented for object-dtype index *subclasses* so they have
    # a chance to implement ops before we unwrap them.
    # See https://github.com/pandas-dev/pandas/issues/31109
    exit(NotImplemented)

exit(super()._arith_method(other, op))
