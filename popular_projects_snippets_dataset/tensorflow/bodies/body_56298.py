# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/load_library.py
"""Loads a TensorFlow PluggableDevice plugin.

  "library_location" can be a path to a specific shared object, or a folder.
  If it is a folder, all shared objects will be loaded. when the library is
  loaded, devices/kernels registered in the library via StreamExecutor C API
  and Kernel/Op Registration C API are made available in TensorFlow process.

  Args:
    library_location: Path to the plugin or folder of plugins. Relative or
      absolute filesystem path to a dynamic library file or folder.

  Raises:
    OSError: When the file to be loaded is not found.
    RuntimeError: when unable to load the library.
  """
if os.path.exists(library_location):
    if os.path.isdir(library_location):
        directory_contents = os.listdir(library_location)

        pluggable_device_libraries = [
            os.path.join(library_location, f)
            for f in directory_contents
            if _is_shared_object(f)
        ]
    else:
        pluggable_device_libraries = [library_location]

    for lib in pluggable_device_libraries:
        py_tf.TF_LoadPluggableDeviceLibrary(lib)
    # Reinitialized physical devices list after plugin registration.
    context.context().reinitialize_physical_devices()
else:
    raise OSError(
        errno.ENOENT,
        'The file or folder to load pluggable device libraries from does not '
        'exist.', library_location)
