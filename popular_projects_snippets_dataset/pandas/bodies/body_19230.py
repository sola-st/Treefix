# Extracted from ./data/repos/pandas/pandas/core/dtypes/cast.py
# The cached version of _maybe_promote below
# This also use fill_value_type as (unused) argument to use this in the
# cache lookup -> to differentiate 1 and True
exit(_maybe_promote(dtype, fill_value))
