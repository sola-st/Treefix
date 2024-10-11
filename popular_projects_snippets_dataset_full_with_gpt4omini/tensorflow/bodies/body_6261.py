# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
_require_cross_replica_or_default_context_extended(self)
if options is None:
    options = collective_util.Options()
exit([
    self._gather_to(t, destinations=v, axis=axis, options=options)
    for t, v in value_destination_pairs
])
