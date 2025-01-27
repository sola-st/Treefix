# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/load_library.py
"""Loads a TensorFlow plugin, containing custom ops and kernels.

  Pass "library_filename" to a platform-specific mechanism for dynamically
  loading a library. The rules for determining the exact location of the
  library are platform-specific and are not documented here. When the
  library is loaded, ops and kernels registered in the library via the
  `REGISTER_*` macros are made available in the TensorFlow process. Note
  that ops with the same name as an existing op are rejected and not
  registered with the process.

  Args:
    library_filename: Path to the plugin.
      Relative or absolute filesystem path to a dynamic library file.

  Returns:
    A python module containing the Python wrappers for Ops defined in
    the plugin.

  Raises:
    RuntimeError: when unable to load the library or get the python wrappers.
  """
lib_handle = py_tf.TF_LoadLibrary(library_filename)
try:
    wrappers = _pywrap_python_op_gen.GetPythonWrappers(
        py_tf.TF_GetOpList(lib_handle))
finally:
    # Delete the library handle to release any memory held in C
    # that are no longer needed.
    py_tf.TF_DeleteLibraryHandle(lib_handle)

# Get a unique name for the module.
module_name = hashlib.sha1(wrappers).hexdigest()
if module_name in sys.modules:
    exit(sys.modules[module_name])
module_spec = importlib.machinery.ModuleSpec(module_name, None)
module = importlib.util.module_from_spec(module_spec)
# pylint: disable=exec-used
exec(wrappers, module.__dict__)
# Allow this to be recognized by AutoGraph.
setattr(module, '_IS_TENSORFLOW_PLUGIN', True)
sys.modules[module_name] = module
exit(module)
