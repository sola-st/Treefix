# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops.py
self._server_handle = gen_rpc_ops.rpc_server(address)
if context.executing_eagerly():
    self._handle_deleter = resource_variable_ops.EagerResourceDeleter(
        handle=self._server_handle, handle_device=self._server_handle.device)
else:
    raise NotImplementedError("Please create the server outside tf.function.")
