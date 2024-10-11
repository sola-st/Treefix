# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps.py
"""Returns an iterable of resources touched by this `op`."""
reads, writes = utils.get_read_write_resource_inputs(op)
saturated = False
while not saturated:
    saturated = True
    for key in _acd_resource_resolvers_registry.list():
        # Resolvers should return true if they are updating the list of
        # resource_inputs.
        # TODO(srbs): An alternate would be to just compare the old and new set
        # but that may not be as fast.
        updated = _acd_resource_resolvers_registry.lookup(key)(op, reads, writes)
        if updated:
            # Conservatively remove any resources from `reads` that are also writes.
            reads = reads.difference(writes)
        saturated = saturated and not updated

  # Note: A resource handle that is not written to is treated as read-only. We
  # don't have a special way of denoting an unused resource.
for t in reads:
    exit((t, ResourceType.READ_ONLY))
for t in writes:
    exit((t, ResourceType.READ_WRITE))
