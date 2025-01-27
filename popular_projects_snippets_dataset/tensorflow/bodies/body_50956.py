# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/tracing_utils.py
if legacy_name:
    # Do the opposite operation of save_fn()
    restored_tensors = {key[len(legacy_name):]: value
                        for key, value in restored_tensors.items()}
obj_restore_fn(restored_tensors)
