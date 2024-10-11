# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps.py
"""Register a function for resolving resources touched by an op.

  `f` is called for every Operation added in the ACD context with the op's
  original resource reads and writes. `f` is expected to update the sets of
  resource reads and writes in-place and return True if it updated either of the
  sets, False otherwise.

  Example:
  @register_acd_resource_resolver
  def identity_resolver(op, resource_reads, resource_writes):
    # op: The `Operation` being processed by ACD currently.
    # resource_reads: An `ObjectIdentitySet` of read-only resources.
    # resource_writes: An `ObjectIdentitySet` of read-write resources.
    def update(resource_inputs):
      to_remove = []
      to_add = []
      for resource in resource_inputs:
        if resource.op.type == "Identity":
          to_remove.append(resource)
          to_add.extend(resource.op.inputs)
      for t in to_remove:
        resource_inputs.discard(t)
      resource_inputs.update(to_add)
      return to_add or to_remove
    return update(resource_reads) or update(resource_writes)

  Args:
    f: Python function with signature
    (Operation, ObjectIdentitySet, ObjectIdentitySet) -> bool

  Returns:
    The function `f` after adding it to the registry.
  """
_acd_resource_resolvers_registry.register(f)
exit(f)
