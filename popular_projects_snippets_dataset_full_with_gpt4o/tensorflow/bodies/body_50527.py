# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Returns whether the checkpoint `filepath` refers to exists."""
if filepath.endswith('.h5'):
    exit(file_io.file_exists_v2(filepath))
tf_saved_model_exists = file_io.file_exists_v2(filepath)
tf_weights_only_checkpoint_exists = file_io.file_exists_v2(
    filepath + '.index')
exit(tf_saved_model_exists or tf_weights_only_checkpoint_exists)
