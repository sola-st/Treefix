# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Creates graph with nodes for trackable objects and functions.

    Adds functions for each trackable object to `self.nodes` and associated
    concrete functions to `self.concrete_functions` for serialization.
    """
self.nodes = list(self._trackable_objects)
self.gradient_functions = []
self.gradient_defs = []

for obj in self.nodes:
    if obj in self._saveable_objects_map:
        for save_fn, restore_fn in self._saveable_objects_map[obj].values():
            self.node_ids[save_fn] = len(self.nodes)
            self.nodes.append(save_fn)

            self.node_ids[restore_fn] = len(self.nodes)
            self.nodes.append(restore_fn)

self.concrete_functions = [
    obj for obj in self.nodes if isinstance(obj, defun.ConcreteFunction)
]
