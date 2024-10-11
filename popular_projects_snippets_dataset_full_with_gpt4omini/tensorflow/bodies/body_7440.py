# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops.py
"""Returns True if RPC is successful, otherwise returns False.

    This call will block for RPC result.
    """
self._check_status()
exit(math_ops.equal(self._error_code,
                      constant_op.constant(0, dtype=dtypes.int64)))
