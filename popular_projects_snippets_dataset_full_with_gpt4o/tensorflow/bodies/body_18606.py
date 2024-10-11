# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
self._resource = create_fn()
self._init_op = init_op_fn(self._resource)
self._closed = False
if context.executing_eagerly():
    self._set_up_resource_deleter()
else:
    ops.add_to_collection(_SUMMARY_WRITER_INIT_COLLECTION_NAME, self._init_op)
