# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
"""Restores attributes replaced with `_replace_child_layer_functions`."""
for child_layer, fns in original_fns.items():
    with utils.no_automatic_dependency_tracking_scope(child_layer):
        for fn_name, fn in fns.items():
            try:
                setattr(child_layer, fn_name, fn)  # pylint: disable=protected-access
            except AttributeError:
                pass  # In the case of _activity_regularizer, setting the attribute
                # may be disallowed.
