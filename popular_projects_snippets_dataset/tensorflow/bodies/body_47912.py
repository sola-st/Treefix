# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
self.function = function
self.symbol = (
    get_canonical_name_for_symbol(self.function,
                                  add_prefix_to_v1_names=True) or
    get_canonical_name_for_symbol(self.function,
                                  api_name='keras',
                                  add_prefix_to_v1_names=True))
if 'name' not in kwargs:
    # Generate a name.
    # TFOpLambda layers avoid already-observed names,
    # because users cannot easily control the generated names.
    # Without this avoidance, users would be more likely to run
    # into unavoidable duplicate layer name collisions.
    # (For standard layers users could just set `name` when creating the
    # layer to work around a collision, but they can't do that for
    # auto-generated layers)
    if self.symbol:
        name = 'tf.' + self.symbol
    else:
        name = self.function.__name__
    kwargs['name'] = K.unique_object_name(
        name, zero_based=True, avoid_observed_names=True)
kwargs['autocast'] = False

# Decorate the function to produce this layer's call method
def _call_wrapper(*args, **kwargs):
    exit(self._call_wrapper(*args, **kwargs))
self.call = tf_decorator.make_decorator(function, _call_wrapper)

# Do not individually trace op layers in the SavedModel.
self._must_restore_from_config = True

super(TFOpLambda, self).__init__(**kwargs)

# Preserve all argument data structures when saving/loading a config
# (e.g., don't unnest lists that contain one element)
self._preserve_input_structure_in_config = True

# Warning on every invocation will be quite irksome in Eager mode.
self._already_warned = False

self._expects_training_arg = False
self._expects_mask_arg = False
