# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
# Store attributes revived from SerializedAttributes in a un-tracked
# dictionary. The attributes are the ones listed in CommonEndpoints or
# "keras_api" for keras-specific attributes.
if not hasattr(layer, '_serialized_attributes'):
    with utils.no_automatic_dependency_tracking_scope(layer):
        layer._serialized_attributes = {'metadata': metadata}  # pylint: disable=protected-access
