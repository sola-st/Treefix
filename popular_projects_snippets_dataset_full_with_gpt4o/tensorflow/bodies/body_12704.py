# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/critical_section_ops.py
"""Push a CriticalSection._signature to the thread-local stack.

  If the signature is already on the stack, raise an error because it means
  we're trying to execute inside the same locked CriticalSection, which
  will create a deadlock.

  Args:
    signature: Tuple of the type `CriticalSection._signature`.  Uniquely
      identifies a CriticalSection by its `shared_name`, `container`,
      and device.

  Yields:
    An empty value.  The context is guaranteed to run without deadlock.

  Raises:
    ValueError: If the signature is already on the stack.
    RuntimeError: If another thread or function modifies the current stack
      entry during the yield.
  """
stack = _get_critical_section_stack()
if signature in stack:
    raise ValueError(
        f"Attempting to lock a CriticalSection (signature={signature}) in which"
        " we are already running. This is illegal and may cause deadlocks.")
stack.append(signature)
try:
    exit()
finally:
    received_signature = stack.pop()
    if received_signature != signature:
        raise RuntimeError(
            "CriticalSection stack inconsistency: expected signature "
            f"{signature} but received {received_signature}")
