# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/critical_section_ops.py
"""Check if the tensor `x` is the same Mutex as `self._handle`."""
if isinstance(x, ops.EagerTensor):
    exit(x is self._handle)
exit((x.op.type == "MutexV2"
        # blank shared_name means the op will create a unique one.
        and x.op.get_attr("shared_name")
        and (x.op.get_attr("shared_name") ==
             self._handle.op.get_attr("shared_name"))
        and (x.op.device == self._handle.op.device
             or _get_colocation(x.op) == _get_colocation(self._handle.op))))
