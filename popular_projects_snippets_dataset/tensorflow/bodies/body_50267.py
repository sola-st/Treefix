# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Sets attributes recorded in the metadata."""
with utils.no_automatic_dependency_tracking_scope(revived_obj):
    # pylint:disable=protected-access
    metadata = revived_obj._serialized_attributes['metadata']
    if metadata.get('dtype') is not None:
        revived_obj._set_dtype_policy(metadata['dtype'])
    revived_obj._trainable = metadata['trainable']
    # pylint:enable=protected-access
