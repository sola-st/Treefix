# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework.py
"""Constructor of `OnRunStartResponse`.

    Args:
      action: (`OnRunStartAction`) the action actually taken by the wrapped
        session for the run() call.
      debug_urls: (`list` of `str`) debug_urls used in watching the tensors
        during the run() call.
      debug_ops: (`str` or `list` of `str`) Debug op(s) to be used by the
        debugger.
      node_name_regex_allowlist: Regular-expression allowlist for node
        name.
      op_type_regex_allowlist: Regular-expression allowlist for op type.
      tensor_dtype_regex_allowlist: Regular-expression allowlist for tensor
        dtype.
      tolerate_debug_op_creation_failures: Whether debug op creation failures
        are to be tolerated.
    """

_check_type(action, str)
self.action = action

_check_type(debug_urls, list)
self.debug_urls = debug_urls

self.debug_ops = debug_ops

self.node_name_regex_allowlist = node_name_regex_allowlist
self.op_type_regex_allowlist = op_type_regex_allowlist
self.tensor_dtype_regex_allowlist = tensor_dtype_regex_allowlist
self.tolerate_debug_op_creation_failures = (
    tolerate_debug_op_creation_failures)
