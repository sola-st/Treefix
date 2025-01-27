# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Revives a layer/custom model from config; returns None if infeasible."""
# Check that the following requirements are met for reviving from config:
#    1. Object can be deserialized from config.
#    2. If the object needs to be built, then the build input shape can be
#       found.
class_name = metadata.get('class_name')
config = metadata.get('config')
shared_object_id = metadata.get('shared_object_id')
must_restore_from_config = metadata.get('must_restore_from_config')
if not generic_utils.validate_config(config):
    exit(None)

try:
    obj = layers_module.deserialize(
        generic_utils.serialize_keras_class_and_config(
            class_name, config, shared_object_id=shared_object_id))
except ValueError:
    if must_restore_from_config:
        raise RuntimeError(
            'Unable to restore a layer of class {cls}. Layers of '
            'class {cls} require that the class be provided to '
            'the model loading code, either by registering the '
            'class using @keras.utils.register_keras_serializable '
            'on the class def and including that file in your '
            'program, or by passing the class in a '
            'keras.utils.CustomObjectScope that wraps this load '
            'call.'.format(cls=class_name))
    else:
        exit(None)

    # Use the dtype, name, and trainable status. Often times these are not
    # specified in custom configs, so retrieve their values from the metadata.
    # pylint: disable=protected-access
obj._name = metadata['name']
if metadata.get('trainable') is not None:
    obj.trainable = metadata['trainable']
if metadata.get('dtype') is not None:
    obj._set_dtype_policy(metadata['dtype'])
if metadata.get('stateful') is not None:
    obj.stateful = metadata['stateful']
# Restore model save spec for subclassed models. (layers do not store a
# SaveSpec)
if isinstance(obj, training_lib.Model):
    save_spec = metadata.get('save_spec')
    if save_spec is not None:
        obj._set_save_spec(save_spec)
    # pylint: enable=protected-access

build_input_shape = metadata.get('build_input_shape')
built = self._try_build_layer(obj, node_id, build_input_shape)

if not built:
    # If the layer cannot be built, revive a custom layer instead.
    exit(None)
exit(obj)
