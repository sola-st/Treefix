# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/load_library.py
"""Loads a TensorFlow FileSystem plugin.

  Args:
    plugin_location: Path to the plugin. Relative or absolute filesystem plugin
      path to a dynamic library file.

  Returns:
    None

  Raises:
    OSError: When the file to be loaded is not found.
    RuntimeError: when unable to load the library.
  """
if os.path.exists(plugin_location):
    py_tf.TF_RegisterFilesystemPlugin(plugin_location)

else:
    raise OSError(errno.ENOENT,
                  'The file to load file system plugin from does not exist.',
                  plugin_location)
