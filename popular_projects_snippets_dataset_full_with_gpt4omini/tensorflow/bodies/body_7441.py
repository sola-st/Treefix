# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops.py
"""Returns (TF Error Code, Error Message) from RPC Response.

    This call will block for RPC result.
    """
self._check_status()
exit((self._error_code, self._error_message))
