# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Setter function that saves some attributes to separate dictionary."""
# Many attributes in the SavedModel conflict with properties defined in
# Layer and Model. Save these attributes to a separate dictionary.
if name in PUBLIC_ATTRIBUTES:
    # pylint: disable=protected-access
    if isinstance(value, trackable.Trackable):
        layer._track_trackable(value, name=name)
    layer._serialized_attributes[name] = value
    # pylint: enable=protected-access
elif (isinstance(layer, functional_lib.Functional) and
      re.match(r'^layer(_with_weights)?-[\d+]', name) is not None):
    # Edges named "layer-n" or "layer_with_weights-n", which are tracked in
    # network._track_layers, should not be added as an attribute. They should
    # be temporarily added as a dependency so that checkpointed values can be
    # restored. These dependencies are manually deleted in
    # KerasObjectLoader.del_tracking.

    # Set `overwrite=True` in the case that `layer` already tracks a different
    # layer-n. This may cause variable values to not be loaded properly in the
    # original layer-n, but we already warn the users about this
    # (ctrl-f "shared between different layers/models").
    layer._track_trackable(value, name, overwrite=True)  # pylint: disable=protected-access
elif getattr(layer, name, None) is not None:
    # Don't overwrite already defined attributes.
    pass
else:
    setattr(layer, name, value)
