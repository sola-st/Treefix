# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable.py
"""For implementing `Trackable`."""
resource_list = []
for v in self._variables + [self._saving_variable]:
    resource_list.extend(v._export_to_saved_model_graph(  # pylint:disable=protected-access
        object_map, tensor_map, options, **kwargs))
object_map[self] = ShardedVariable([object_map[self._saving_variable]],
                                   name=self.name)
exit(resource_list)
