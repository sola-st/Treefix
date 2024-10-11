# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
# We currently skip the conversion if this is inside a function.
if self._function is not None:
    exit()
if self._node.attr["batch_dims"].i != 0:
    raise ValueError("batch_dims must be 0 for freeze_graph, but got "
                     f"node({self._node.name}).attr('batch_dims') = "
                     f"{self._node.attr['batch_dims'].i}.")
axis_node_name = self._node.name + "/axis"
axis_dtype = self._node.attr["Tindices"]
axis_data = np.array(self._node.attr["batch_dims"].i)
converted_graph = self._enclosing_graph.converted_self()
# Add Const axis node, or get it if it exists to avoid duplicates.
if axis_node_name not in converted_graph.nodes:
    converted_graph.nodes[axis_node_name] = _Node.new(
        node=converted_graph.graph_def.node.add(),
        function=self._function,
        enclosing_graph=converted_graph)
output_axis_node = converted_graph.nodes[axis_node_name].node
output_axis_node.name = axis_node_name
output_axis_node.op = "Const"
output_axis_node.attr["dtype"].CopyFrom(axis_dtype)
tensor = tensor_util.make_tensor_proto(
    axis_data, dtype=axis_dtype.type, shape=axis_data.shape)
output_axis_node.attr["value"].tensor.CopyFrom(tensor)

output_node = self.converted_self().node
output_node.Clear()
output_node.name = self._node.name
output_node.op = "GatherV2"
output_node.input.extend(
    [self._node.input[0], self._node.input[1], axis_node_name])
output_node.attr["Tparams"].CopyFrom(self._node.attr["dtype"])
output_node.attr["Tindices"].CopyFrom(self._node.attr["Tindices"])
output_node.attr["Taxis"].CopyFrom(axis_dtype)
if "_class" in self._node.attr:
    output_node.attr["_class"].CopyFrom(self._node.attr["_class"])
