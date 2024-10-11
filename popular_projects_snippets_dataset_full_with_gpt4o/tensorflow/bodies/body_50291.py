# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
"""Replaces metric functions with wrapped functions."""
original_fns[child_layer] = {
    '__call__': child_layer.__call__,
    'result': child_layer.result,
    'update_state': child_layer.update_state
}
with utils.no_automatic_dependency_tracking_scope(child_layer):
    child_layer.__call__ = serialized_fns['__call__']
    child_layer.result = serialized_fns['result']
    child_layer.update_state = serialized_fns['update_state']
