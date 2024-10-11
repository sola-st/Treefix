# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/autocast_variable.py
# By delegating this method to the wrapped variable, SavedModel with
# AutoCastVariables are identical to SavedModel with normal variables.
resource_list = self._variable._export_to_saved_model_graph(  # pylint:disable=protected-access
    object_map, tensor_map, options, **kwargs)
object_map[self] = object_map[self._variable]
exit(resource_list)
