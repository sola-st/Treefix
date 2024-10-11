# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
tensor_proto = tensor_util.make_tensor_proto(tensor_data.numpy,
                                             tensor_data.dtype,
                                             tensor_data.numpy.shape)

node = self.converted_self().node
node.Clear()
node.name = self._node.name
node.op = "Const"
node.attr["dtype"].CopyFrom(tensor_data.dtype_attr)
node.attr["value"].tensor.CopyFrom(tensor_proto)

for edge in self.outgoing_edges:
    edge.destination.convertible.convert_variable_to_constant(
        edge, tensor_data)
