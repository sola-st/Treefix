# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/critical_section_ops.py
"""Raise if captured_resources are accessed by another CriticalSection.

    Args:
      captured_resources: Set of tensors of type resource.
      exclusive_resource_access: Whether this execution requires exclusive
        resource access.

    Raises:
      ValueError: If any tensors in `captured_resources` are also accessed
        by another `CriticalSection`, and at least one of them requires
        exclusive resource access.
    """
# Collections and op introspection does not work in eager
# mode.  This is generally ok; since eager mode (as of
# writing) executes sequentially anyway.
for sg in ops.get_collection(CRITICAL_SECTION_EXECUTIONS):
    if self._is_self_handle(sg.handle):
        # Other executions in the same critical section are allowed.
        continue
    if not (exclusive_resource_access or sg.exclusive_resource_access):
        # Neither execution requested exclusive access.
        continue
    resource_intersection = captured_resources.intersection(sg.resources)
    if resource_intersection:
        raise ValueError(
            "This execution would access resources: "
            f"{list(resource_intersection)}. Either this lock "
            f"(CriticalSection: {self._handle}) or lock '{sg}' "
            f"(CriticalSection: {sg.handle}) requested exclusive resource "
            "access of this resource. Did you mean to call execute with "
            "keyword argument exclusive_resource_access=False?")
