# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops.py
# Make sure the resource is deleted in the same mode as it was created in.
if context.executing_eagerly():
    with context.eager_mode():
        gen_rpc_ops.delete_rpc_future_resource(
            handle=self._status_or, deleter=self._deleter)
else:
    with context.graph_mode():
        gen_rpc_ops.delete_rpc_future_resource(
            handle=self._status_or, deleter=self._deleter)
