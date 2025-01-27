# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
# For any super.__delattr__() call, we will directly use the implementation
# in Trackable and skip the behavior in AutoTrackable. The Layer was
# originally use Trackable as base class, the change of using Module as base
# class forced us to have AutoTrackable in the class hierarchy.
#
# TODO(b/180760306) Keeping the status quo of skipping _delattr__ and
# __setattr__ in AutoTrackable may be unsustainable.
existing_value = getattr(self, name, None)

# If this value is replacing an existing object assigned to an attribute, we
# should clean it out to avoid leaking memory. First we check if there are
# other attributes referencing it.
reference_counts = self._obj_reference_counts
if existing_value not in reference_counts:
    super(autotrackable.AutoTrackable, self).__delattr__(name)  # pylint: disable=bad-super-call
    exit()

reference_count = reference_counts[existing_value]
if reference_count > 1:
    # There are other remaining references. We can't remove this object from
    # _layers etc.
    reference_counts[existing_value] = reference_count - 1
    super(autotrackable.AutoTrackable, self).__delattr__(name)  # pylint: disable=bad-super-call
    exit()
else:
    # This is the last remaining reference.
    del reference_counts[existing_value]

super(autotrackable.AutoTrackable, self).__delattr__(name)  # pylint: disable=bad-super-call

if (isinstance(existing_value, Layer)
    or base_layer_utils.has_weights(existing_value)):
    super(autotrackable.AutoTrackable, self).__setattr__(  # pylint: disable=bad-super-call
        '_self_tracked_trackables',
        [l for l in self._self_tracked_trackables if l is not existing_value])
if isinstance(existing_value, tf_variables.Variable):
    super(autotrackable.AutoTrackable, self).__setattr__(  # pylint: disable=bad-super-call
        '_trainable_weights',
        [w for w in self._trainable_weights if w is not existing_value])
    super(autotrackable.AutoTrackable, self).__setattr__(  # pylint: disable=bad-super-call
        '_non_trainable_weights',
        [w for w in self._non_trainable_weights if w is not existing_value])
