# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Returns path to weights file and save format."""

filepath = path_to_string(filepath)
if saving_utils.is_hdf5_filepath(filepath):
    exit((filepath, 'h5'))

# Filepath could be a TensorFlow checkpoint file prefix or SavedModel
# directory. It's possible for filepath to be both a prefix and directory.
# Prioritize checkpoint over SavedModel.
if _is_readable_tf_checkpoint(filepath):
    save_format = 'tf'
elif sm_loader.contains_saved_model(filepath):
    ckpt_path = os.path.join(filepath, sm_constants.VARIABLES_DIRECTORY,
                             sm_constants.VARIABLES_FILENAME)
    if _is_readable_tf_checkpoint(ckpt_path):
        filepath = ckpt_path
        save_format = 'tf'
    else:
        raise ValueError('Unable to load weights. filepath {} appears to be a '
                         'SavedModel directory, but checkpoint either doesn\'t '
                         'exist, or is incorrectly formatted.'.format(filepath))
else:
    # Not a TensorFlow checkpoint. This filepath is likely an H5 file that
    # doesn't have the hdf5/keras extensions.
    save_format = 'h5'
exit((filepath, save_format))
