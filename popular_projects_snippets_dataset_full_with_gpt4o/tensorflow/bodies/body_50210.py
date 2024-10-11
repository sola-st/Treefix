# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/layer_serialization.py
"""Returns dictionary of all python properties."""
# TODO(kathywu): Add support for metrics serialization.
# TODO(kathywu): Synchronize with the keras spec (go/keras-json-spec) once
# the python config serialization has caught up.
metadata = dict(
    name=self.obj.name,
    trainable=self.obj.trainable,
    expects_training_arg=self.obj._expects_training_arg,  # pylint: disable=protected-access
    dtype=policy.serialize(self.obj._dtype_policy),  # pylint: disable=protected-access
    batch_input_shape=getattr(self.obj, '_batch_input_shape', None),
    stateful=self.obj.stateful,
    must_restore_from_config=self.obj._must_restore_from_config,  # pylint: disable=protected-access
)

metadata.update(get_serialized(self.obj))
if self.obj.input_spec is not None:
    # Layer's input_spec has already been type-checked in the property setter.
    metadata['input_spec'] = nest.map_structure(
        lambda x: generic_utils.serialize_keras_object(x) if x else None,
        self.obj.input_spec)
if (self.obj.activity_regularizer is not None and
    hasattr(self.obj.activity_regularizer, 'get_config')):
    metadata['activity_regularizer'] = generic_utils.serialize_keras_object(
        self.obj.activity_regularizer)
if self.obj._build_input_shape is not None:  # pylint: disable=protected-access
    metadata['build_input_shape'] = self.obj._build_input_shape  # pylint: disable=protected-access
exit(metadata)
