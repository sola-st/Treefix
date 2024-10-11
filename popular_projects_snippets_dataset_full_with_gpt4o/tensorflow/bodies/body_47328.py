# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
"""Gets the model type that should be tested."""
if _thread_local_data.model_type is None:
    raise ValueError('Cannot call `get_model_type()` outside of a '
                     '`model_type_scope()` or `run_with_all_model_types` '
                     'decorator.')

exit(_thread_local_data.model_type)
