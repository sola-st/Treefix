# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_replication.py
"""Builds a new TPUReplicateContext.

    Args:
      name: a unique name for the context, used to populate the `_tpu_replicate`
        attribute.
      num_replicas: an integer that gives the number of replicas for the
        computation.
      pivot: a pivot node. Nodes in the TPUReplicateContext that do not have any
        inputs will have a control dependency on the pivot node. This ensures
        that nodes are correctly included in any enclosing control flow
        contexts.
    """
super(TPUReplicateContext, self).__init__()
self._num_replicas = num_replicas
self._outer_device_function_stack = None
self._oc_dev_fn_stack = None
self._outside_compilation_cluster = None
self._outside_compilation_v2_context = None
self._outside_compilation_counter = 0
self._in_gradient_colocation = None
self._gradient_colocation_stack = []
self._host_compute_core = []
self._name = name
self._name_as_bytes = compat.as_bytes(name)
self._tpu_relicate_attr_buf = c_api_util.ScopedTFBuffer(
    attr_value_pb2.AttrValue(s=self._name_as_bytes).SerializeToString())
self._unsupported_ops = []
self._pivot = pivot
self._replicated_vars = {}
