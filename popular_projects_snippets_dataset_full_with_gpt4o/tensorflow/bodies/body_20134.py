# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_feed.py
"""Freezes the InfeedQueue so it can no longer be modified.

    The configuration is implicitly frozen before any host-side or
    device-side Ops are generated. The configuration cannot be frozen
    until the types and shapes of the tuple elements have been set.

    Raises:
      ValueError: if the types or shapes of the tuple elements have not been
      set.
    """
self._frozen = True
if self._tuple_types is None:
    raise ValueError(
        "Can't freeze an InfeedQueue without setting all tuple types.")
if self._tuple_shapes is None:
    raise ValueError(
        "Can't freeze an InfeedQueue without setting all tuple shapes.")
for shape in self._tuple_shapes:
    if shape.dims is None:
        raise ValueError(
            "Can't freeze an InfeedQueue without setting all tuple shapes.")
for policy in self._sharding_policies:
    policy.freeze()
self._validate()
