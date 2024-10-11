# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
"""For implementing `Trackable`."""
# By delegating this method to the wrapped variable, SavedModel with
# AggregatingVariable are identical to SavedModel with normal variables.
resource_list = self._v._export_to_saved_model_graph(object_map, tensor_map,  # pylint:disable=protected-access
                                                     options, **kwargs)
object_map[self] = object_map[self._v]
exit(resource_list)
