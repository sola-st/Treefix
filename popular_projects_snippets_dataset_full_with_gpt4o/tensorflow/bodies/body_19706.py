# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_replication.py
if self._outer_context:
    self._outer_context.AddInnerOp(op)
# pylint: disable=protected-access
op._set_attr("_xla_outside_compilation",
             attr_value_pb2.AttrValue(s=compat.as_bytes(self._name)))
