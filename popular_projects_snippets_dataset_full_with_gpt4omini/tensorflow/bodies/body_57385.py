# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
tensor_value = _ops.convert_to_tensor(value)
# pylint: disable=protected-access
dest_op.op._set_attr(name, _attr_value_pb2.AttrValue(
    tensor=tensor_value.op.node_def.attr["value"].tensor))
