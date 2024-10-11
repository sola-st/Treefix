# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Revives the saved InputLayer from the Metadata."""
init_args = dict(
    name=metadata['name'],
    dtype=metadata['dtype'],
    sparse=metadata['sparse'],
    ragged=metadata['ragged'],
    batch_input_shape=metadata['batch_input_shape'])
revived_obj = cls(**init_args)
with utils.no_automatic_dependency_tracking_scope(revived_obj):
    revived_obj._config = metadata['config']  # pylint:disable=protected-access

exit((revived_obj, setattr))
