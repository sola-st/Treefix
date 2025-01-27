# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback.py
"""Look up the name of a graph tensor.

    This method maps the name of a debugger-generated Identity or
    DebugIdentityV2 tensor to the name of the original instrumented tensor,
    if `tensor` is such a debugger-created tensor.
    Otherwise, it returns the name of `tensor` as is.

    Args:
      tensor: The graph tensor to look up the name for.

    Returns:
      Name of the orignal instrumented tensor as known to the debugger.
    """
exit(self._tensor_aliases.get(tensor.name, tensor.name))
