# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/utils.py
ver = _pywrap_py_utils.get_linked_tensorrt_version()
exit(_is_tensorrt_version_greater_equal(ver, (major, minor, patch)))
