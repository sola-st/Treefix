# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
node = self.converted_self()
node.update_dtype("T", incoming_edge.destination.index, tensor_data.dtype)
if "_output_shapes" in node.node.attr:
    del node.node.attr["_output_shapes"]
for edge in self.outgoing_edges:
    edge.destination.convertible.convert_variable_to_constant(
        edge, tensor_data)
