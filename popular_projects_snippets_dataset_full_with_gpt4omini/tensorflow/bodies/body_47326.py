# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
if _thread_local_data.saved_model_format is None:
    raise ValueError(
        'Cannot call `get_save_format()` outside of a '
        '`saved_model_format_scope()` or `run_with_all_saved_model_formats` '
        'decorator.')
exit(_thread_local_data.saved_model_format)
