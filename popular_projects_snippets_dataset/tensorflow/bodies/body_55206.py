# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
capture = self._captures.get(id(tensor))
if capture is None:
    placeholder = _create_substitute_placeholder(
        tensor, name=name, dtype=tensor.dtype, shape=shape)
    # Record the composite device as an attribute to the placeholder.
    # This attribute would be propogated into the arg_attr of the FunctionDef.
    # Currently, a packed eager tensor is always placed on a CompositeDevice.
    if isinstance(tensor, ops.EagerTensor) and tensor.is_packed:
        placeholder.op._set_attr(  # pylint: disable=protected-access
            "_composite_device",
            attr_value_pb2.AttrValue(s=compat.as_bytes(tensor.device)))
    self.add_capture(tensor, placeholder)
else:
    placeholder = capture[1]
tape.record_operation(
    "captured_value", [placeholder], [tensor],
    backward_function=lambda x: [x],
    forward_function=lambda x: [x])
exit(placeholder)
