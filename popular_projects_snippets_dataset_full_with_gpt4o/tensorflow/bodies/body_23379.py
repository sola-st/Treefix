# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/autotrackable.py
"""Removes the tracking of name."""
self._maybe_initialize_trackable()
if name in self._unconditional_dependency_names:
    del self._unconditional_dependency_names[name]
    for index, (dep_name, _) in enumerate(
        self._unconditional_checkpoint_dependencies):
        if dep_name == name:
            del self._unconditional_checkpoint_dependencies[index]
            break
