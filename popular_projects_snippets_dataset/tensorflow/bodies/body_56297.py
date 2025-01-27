# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/load_library.py
"""Loads a TensorFlow plugin.

  "library_location" can be a path to a specific shared object, or a folder.
  If it is a folder, all shared objects that are named "libtfkernel*" will be
  loaded. When the library is loaded, kernels registered in the library via the
  `REGISTER_*` macros are made available in the TensorFlow process.

  Args:
    library_location: Path to the plugin or the folder of plugins.
      Relative or absolute filesystem path to a dynamic library file or folder.

  Returns:
    None

  Raises:
    OSError: When the file to be loaded is not found.
    RuntimeError: when unable to load the library.
  """
if os.path.exists(library_location):
    if os.path.isdir(library_location):
        directory_contents = os.listdir(library_location)

        kernel_libraries = [
            os.path.join(library_location, f) for f in directory_contents
            if _is_shared_object(f)]
    else:
        kernel_libraries = [library_location]

    for lib in kernel_libraries:
        py_tf.TF_LoadLibrary(lib)

else:
    raise OSError(
        errno.ENOENT,
        'The file or folder to load kernel libraries from does not exist.',
        library_location)
