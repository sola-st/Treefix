# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops.py
if self._error_code is None:
    self._error_code, self._error_message = gen_rpc_ops.rpc_check_status(
        self._status_or)
