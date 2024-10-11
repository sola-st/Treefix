# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/policy.py
"""A context manager that sets the global Policy under it.

  Args:
    policy: A Policy, or a string that will be converted to a Policy..

  Yields:
    Nothing.
  """
old_policy = _global_policy
try:
    set_global_policy(policy)
    exit()
finally:
    set_global_policy(old_policy)
