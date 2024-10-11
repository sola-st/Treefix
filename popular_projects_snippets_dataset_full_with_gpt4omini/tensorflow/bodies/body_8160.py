# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_replicated_variable.py
"""For implementing `Trackable`."""
first_var = self._vars[0]
resource_list = first_var._export_to_saved_model_graph(  # pylint:disable=protected-access
    object_map, tensor_map, options, **kwargs)
for v in self._vars[1:]:
    object_map[v] = object_map[first_var]
    tensor_map[v.handle] = tensor_map[first_var.handle]
    resource_list.append(v.handle)
object_map[self] = object_map[first_var]
tensor_map[self] = tensor_map[first_var.handle]
resource_list.append(self)
exit(resource_list)
