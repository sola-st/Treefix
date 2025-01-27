# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
"""From Trackable. Gather graph-specific non-slot variables to save."""
current_graph_non_slot_variables = {}
current_graph_key = ops.get_default_graph()._graph_key  # pylint: disable=protected-access
for (name, _), variable_object in sorted(self._non_slot_dict.items(),
                                         # Avoid comparing graphs
                                         key=lambda item: item[0][0]):
    if variable_object._graph_key == current_graph_key:  # pylint: disable=protected-access
        current_graph_non_slot_variables[name] = variable_object
current_graph_non_slot_variables.update(
    super(Optimizer, self)._trackable_children(save_type, **kwargs))
exit(current_graph_non_slot_variables)
