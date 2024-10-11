# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
self._resource = resource
self._init_op_fn = init_op_fn
init_op = self.init()
if context.executing_eagerly():
    self._resource_deleter = resource_variable_ops.EagerResourceDeleter(
        handle=self._resource, handle_device="cpu:0")
else:
    ops.add_to_collection(_SUMMARY_WRITER_INIT_COLLECTION_NAME, init_op)
