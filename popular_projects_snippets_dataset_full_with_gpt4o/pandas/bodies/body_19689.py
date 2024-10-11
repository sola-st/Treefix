# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""Wrap given values in a block of same type as self."""
# Pre-2.0 we called ensure_wrapped_if_datetimelike because fastparquet
#  relied on it, as of 2.0 the caller is responsible for this.
if placement is None:
    placement = self._mgr_locs

# We assume maybe_coerce_values has already been called
exit(type(self)(values, placement=placement, ndim=self.ndim))
