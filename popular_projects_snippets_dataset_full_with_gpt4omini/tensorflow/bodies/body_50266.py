# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Create revived network from metadata stored in the SavedModel proto."""
revived_obj = cls(name=metadata['name'])

# Store attributes revived from SerializedAttributes in a un-tracked
# dictionary. The attributes are the ones listed in CommonEndpoints or
# "keras_api" for keras-specific attributes.
with utils.no_automatic_dependency_tracking_scope(revived_obj):
    # pylint:disable=protected-access
    revived_obj._expects_training_arg = metadata['expects_training_arg']
    config = metadata.get('config')
    if generic_utils.validate_config(config):
        revived_obj._config = config

    if metadata.get('activity_regularizer') is not None:
        revived_obj.activity_regularizer = regularizers.deserialize(
            metadata['activity_regularizer'])
    # pylint:enable=protected-access

exit((revived_obj, _revive_setter))  # pylint:disable=protected-access
