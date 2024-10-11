# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib.py
# At shutdown, `errors` may have been garbage collected.
if errors is not None:
    exception = errors.UnimplementedError
else:
    exception = Exception
try:
    c_api.TF_ServerStop(self._server)
    # Clean shutdown of servers is not yet implemented, so
    # we leak instead of calling c_api.TF_DeleteServer here.
    # See:
    # https://github.com/tensorflow/tensorflow/blob/0495317a6e9dd4cac577b9d5cf9525e62b571018/tensorflow/core/distributed_runtime/rpc/grpc_server_lib.h#L73
except AttributeError:
    # At shutdown, `c_api` may have been garbage collected.
    pass
except exception:
    pass
self._server = None
