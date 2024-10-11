# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
super(_While, self).convert_variable_to_constant(incoming_edge, tensor_data)
node = self.converted_self()
if node.node.attr["output_shapes"].list.shape:
    node.node.attr["output_shapes"].list.shape[
        incoming_edge.destination.index].CopyFrom(
            tensor_shape_pb2.TensorShapeProto(dim=[
                tensor_shape_pb2.TensorShapeProto.Dim(size=dim)
                for dim in tensor_data.numpy.shape
            ]))

# The while's body inputs and outputs have the same type, so here we can go
# ahead and change that function's output type.
body_name = self._node.attr["body"].func.name
body = self._enclosing_graph.functions[body_name].converted_self().function
body.signature.output_arg[
    incoming_edge.destination.index].type = tensor_data.dtype
