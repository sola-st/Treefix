# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Create revived layer from metadata stored in the SavedModel proto."""
init_args = dict(
    name=metadata['name'],
    trainable=metadata['trainable'])
if metadata.get('dtype') is not None:
    init_args['dtype'] = metadata['dtype']
if metadata.get('batch_input_shape') is not None:
    init_args['batch_input_shape'] = metadata['batch_input_shape']

revived_obj = cls(**init_args)

with utils.no_automatic_dependency_tracking_scope(revived_obj):
    # pylint:disable=protected-access
    revived_obj._expects_training_arg = metadata['expects_training_arg']
    config = metadata.get('config')
    if generic_utils.validate_config(config):
        revived_obj._config = config
    if metadata.get('input_spec') is not None:
        revived_obj.input_spec = recursively_deserialize_keras_object(
            metadata['input_spec'],
            module_objects={'InputSpec': input_spec.InputSpec})
    if metadata.get('activity_regularizer') is not None:
        revived_obj.activity_regularizer = regularizers.deserialize(
            metadata['activity_regularizer'])
    if metadata.get('_is_feature_layer') is not None:
        revived_obj._is_feature_layer = metadata['_is_feature_layer']
    if metadata.get('stateful') is not None:
        revived_obj.stateful = metadata['stateful']
    # pylint:enable=protected-access

exit((revived_obj, _revive_setter))
