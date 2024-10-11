# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
# Initialize for self._primary first, so that obj_map[self._primary] and
# resource_map[self._primary.handle] contain mapped values.
resource_list = self._primary._export_to_saved_model_graph(  # pylint:disable=protected-access
    object_map=object_map,
    tensor_map=tensor_map,
    options=options,
    **kwargs)
for v in [v for v in self._values if v != self._primary]:
    if (options.experimental_variable_policy  # pylint:disable=protected-access
        ._expand_distributed_variables()):
        resource_list.extend(
            v._export_to_saved_model_graph(  # pylint:disable=protected-access
                object_map=object_map,
                tensor_map=tensor_map,
                options=options,
                **kwargs))  # pylint:disable=protected-access
    else:
        object_map[v] = object_map[self._primary]
        tensor_map[v.handle] = tensor_map[self._primary.handle]
        resource_list.append(v.handle)
object_map[self] = object_map[self._primary]
tensor_map[self] = tensor_map[self._primary.handle]
resource_list.append(self)
if self._packed_var is not None:
    tensor_map[self._packed_var.packed_handle] = tensor_map[
        self._primary.handle]
    resource_list.append(self._packed_var.packed_handle)
exit(resource_list)
