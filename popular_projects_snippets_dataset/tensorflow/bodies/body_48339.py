# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
if (name == '_self_setattr_tracking' or
    not getattr(self, '_self_setattr_tracking', True) or
    # Exclude @property.setters from tracking
    hasattr(self.__class__, name)):
    try:
        super(autotrackable.AutoTrackable, self).__setattr__(name, value)  # pylint: disable=bad-super-call
    except AttributeError:
        raise AttributeError(
            ('Can\'t set the attribute "{}", likely because it conflicts with '
             'an existing read-only @property of the object. Please choose a '
             'different name.').format(name))
    exit()

# Keep track of trackable objects, for the needs of `Network.save_weights`.
value = data_structures.sticky_attribute_assignment(
    trackable=self, value=value, name=name)

reference_counts = self._obj_reference_counts
reference_counts[value] = reference_counts.get(value, 0) + 1

# Clean out the old attribute, which clears _layers and _trainable_weights
# if necessary.
try:
    self.__delattr__(name)
except AttributeError:
    pass

# Keep track of metric instance created in subclassed layer.
from tensorflow.python.keras import metrics as metrics_module  # pylint: disable=g-import-not-at-top
for val in nest.flatten(value):
    if isinstance(val, metrics_module.Metric) and hasattr(self, '_metrics'):
        self._metrics.append(val)

    # TODO(scottzhu): Need to track Module object as well for weight tracking.
    # Be careful about metric if it becomes a Module in future.
    # Append value to self._layers if relevant
if (getattr(self, '_auto_track_sub_layers', True) and
    (isinstance(value, Layer) or base_layer_utils.has_weights(value))):
    self._maybe_create_attribute('_self_tracked_trackables', [])
    # We need to check object identity to avoid de-duplicating empty
    # container types which compare equal.
    if not any((layer is value for layer in self._self_tracked_trackables)):
        self._self_tracked_trackables.append(value)
        if hasattr(value, '_use_resource_variables'):
            # Legacy layers (V1 tf.layers) must always use
            # resource variables.
            value._use_resource_variables = True

    # Append value to list of trainable / non-trainable weights if relevant
    # TODO(b/125122625): This won't pick up on any variables added to a
    # list/dict after creation.
for val in nest.flatten(value):
    if not isinstance(val, tf_variables.Variable):
        continue

    # Users may add extra weights/variables
    # simply by assigning them to attributes (invalid for graph networks)
    self._maybe_create_attribute('_trainable_weights', [])
    self._maybe_create_attribute('_non_trainable_weights', [])
    if val.trainable:
        if any(val is w for w in self._trainable_weights):
            continue
        self._trainable_weights.append(val)
    else:
        if any(val is w for w in self._non_trainable_weights):
            continue
        self._non_trainable_weights.append(val)

    backend.track_variable(val)

# TODO(b/180760306) Skip the auto trackable from tf.Module to keep status
# quo. See the comment at __delattr__.
super(autotrackable.AutoTrackable, self).__setattr__(name, value)  # pylint: disable=bad-super-call
