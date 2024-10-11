# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops.py
"""Method to invoke remote registered functions on the connected server.

    Server should be started before making an RPC Call.

    Args:
      method_name: Registered method to invoke on Server.
      args: Input arguments for the method.
      output_specs: Output specs for the output from method.
      timeout_in_ms: Timeout for this call. If 0, default client timeout will be
       used.

    Returns:
      StatusOrResult object. This function issues the RPC call to server, it
      does not block for the duration of RPC. Please call is_ok, get_error or
      get_value methods on the returned object to blocked till RPC finishes.
    """
if args is None:
    args = []
status_or, deleter = gen_rpc_ops.rpc_call(
    self._client_handle,
    args=nest.flatten(args),
    method_name=method_name,
    timeout_in_ms=timeout_in_ms)
exit(StatusOrResult(status_or, deleter, output_specs))
