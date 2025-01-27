# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/models.py
"""Restores the original state of a model after it was "reset".

  This undoes this action of `_in_place_subclassed_model_reset`, which is called
  in `clone_and_build_model` if `in_place_reset` is set to True.

  Args:
    model: Instance of a Keras model created via subclassing, on which
      `_in_place_subclassed_model_reset` was previously called.
  """
assert not model._is_graph_network
# Restore layers and build attributes
if (hasattr(model, '_original_attributes_cache') and
    model._original_attributes_cache is not None):
    # Models have sticky attribute assignment, so we want to be careful to add
    # back the previous attributes and track Layers by their original names
    # without adding dependencies on "utility" attributes which Models exempt
    # when they're constructed.
    setattr_tracking = model._setattr_tracking
    model._setattr_tracking = False
    model._self_tracked_trackables = []
    for name, value in model._original_attributes_cache.items():
        setattr(model, name, value)
        if isinstance(value, Layer):
            model._self_tracked_trackables.append(value)
    model._original_attributes_cache = None
    model._setattr_tracking = setattr_tracking
else:
    # Restore to the state of a never-called model.
    _reset_build_compile_trackers(model)
