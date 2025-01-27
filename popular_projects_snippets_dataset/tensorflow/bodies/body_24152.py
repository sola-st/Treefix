# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework.py
"""Constructor of WatchOptions: Debug watch options.

    Used as return values of `watch_fn`s.

    Args:
      debug_ops: (`str` or `list of str`) Debug ops to be used.
      node_name_regex_allowlist: Regular-expression allowlist for node_name,
        e.g., `"(weight_[0-9]+|bias_.*)"`
      op_type_regex_allowlist: Regular-expression allowlist for the op type of
        nodes, e.g., `"(Variable|Add)"`.
        If both `node_name_regex_allowlist` and `op_type_regex_allowlist`
        are set, the two filtering operations will occur in a logical `AND`
        relation. In other words, a node will be included if and only if it
        hits both allowlists.
      tensor_dtype_regex_allowlist: Regular-expression allowlist for Tensor
        data type, e.g., `"^int.*"`.
        This allowlist operates in logical `AND` relations to the two allowlists
        above.
      tolerate_debug_op_creation_failures: (`bool`) whether debug op creation
        failures (e.g., due to dtype incompatibility) are to be tolerated by not
        throwing exceptions.
    """
if debug_ops:
    self.debug_ops = debug_ops
else:
    self.debug_ops = ["DebugIdentity"]
self.node_name_regex_allowlist = node_name_regex_allowlist
self.op_type_regex_allowlist = op_type_regex_allowlist
self.tensor_dtype_regex_allowlist = tensor_dtype_regex_allowlist
self.tolerate_debug_op_creation_failures = (
    tolerate_debug_op_creation_failures)
