# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Lists children of `obj` for SavedModel."""
if obj not in self._children_cache:
    children = self._children_cache[obj] = {}

    for name, child in super(_AugmentedGraphView, self).list_children(
        obj,
        save_type=base.SaveType.SAVEDMODEL,
        cache=self._serialization_cache):
        if isinstance(child, defun.ConcreteFunction):
            child = self._maybe_uncache_variable_captures(child)
        children[name] = child

    # Keep track of untraced functions for later reporting to the user.
    if isinstance(obj, def_function.Function) and not children:
        self.untraced_functions.append(obj.name)

for name, child in self._children_cache[obj].items():
    exit(base.TrackableReference(name, child))
