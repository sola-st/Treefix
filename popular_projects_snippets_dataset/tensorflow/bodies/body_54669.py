# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
"""Caches the tensor data for all Placeholders in the given function."""
map_index_to_variable = {}
for var in self._func.graph.variables:
    for idx, captured_input in enumerate(self._func.captured_inputs):
        if var.handle is captured_input:  # pylint: disable=protected-access
            map_index_to_variable[idx] = var
            break

    # Iterates through all captures which are represented as Placeholders.
for idx, (val_tensor, name_tensor) in enumerate(self._func.graph.captures):
    tensor_name = name_tensor.name.split(":")[0]
    if not self._should_convert(tensor_name):
        continue
    if idx in map_index_to_variable:
        data = self._eval(map_index_to_variable[idx])
    else:
        if val_tensor.dtype == dtypes.resource:
            logging.vlog(1, "Skip converting resource tensor %s" % tensor_name)
            continue
        data = np.array(self._eval(val_tensor))

    self._tensor_data[tensor_name] = _TensorData(
        numpy=data,
        dtype=dtypes.as_dtype(data.dtype).as_datatype_enum,
        index=idx)

# Get data for VariableV2 ops (reference variables) that cannot be lifted.
for node in self.node_defs.values():
    if node.op == "VariableV2":
        if not self._should_convert(node.name):
            continue
        if node.name not in self.tensor_data:
            with self._func.graph.as_default():
                identity_node = array_ops.identity(
                    self._func.graph.as_graph_element(node.name + ":0"))
            pruned_graph = self._func.prune([], [identity_node.name])()[0]
            self._tensor_data[node.name] = _TensorData(
                numpy=pruned_graph.numpy(),
                dtype=node.attr["dtype"].type,
                index=None)
