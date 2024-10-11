# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
"""Check compatibility of TensorRT version.

  Raises:
    RuntimeError: if the TensorRT library version is incompatible.
  """

if not _pywrap_py_utils.is_tensorrt_enabled():
    logging.error(
        "Tensorflow needs to be built with TensorRT support enabled to allow "
        "TF-TRT to operate.")

    raise RuntimeError("Tensorflow has not been built with TensorRT support.")

if platform.system() == "Windows":
    logging.warn(
        "Windows support is provided experimentally. No guarantee is made "
        "regarding functionality or engineering support. Use at your own risk.")

linked_version = _pywrap_py_utils.get_linked_tensorrt_version()
loaded_version = _pywrap_py_utils.get_loaded_tensorrt_version()

logging.info("Linked TensorRT version: %s", str(linked_version))
logging.info("Loaded TensorRT version: %s", str(loaded_version))

def raise_trt_version_deprecated(version_type, trt_version):
    assert version_type in [
        "linked", "loaded"
    ], ("Incorrect value received for version_type: %s. Accepted: ['linked', "
        "'loaded']") % version_type

    logging.error(
        "The {version_type} version of TensorRT: `{trt_version}` has now "
        "been removed. Please upgrade to TensorRT 7 or more recent.".format(
            version_type=version_type,
            trt_version=trt_utils.version_tuple_to_string(trt_version)))

    raise RuntimeError("Incompatible %s TensorRT versions" % version_type)

if not trt_utils.is_linked_tensorrt_version_greater_equal(7, 0, 0):
    raise_trt_version_deprecated("linked", linked_version)

if not trt_utils.is_loaded_tensorrt_version_greater_equal(7, 0, 0):
    raise_trt_version_deprecated("loaded", loaded_version)

if (loaded_version[0] != linked_version[0] or
    not trt_utils.is_loaded_tensorrt_version_greater_equal(*linked_version)):
    logging.error(
        "Loaded TensorRT %s but linked TensorFlow against TensorRT %s. A few "
        "requirements must be met:\n"
        "\t-It is required to use the same major version of TensorRT during "
        "compilation and runtime.\n"
        "\t-TensorRT does not support forward compatibility. The loaded "
        "version has to be equal or more recent than the linked version.",
        trt_utils.version_tuple_to_string(loaded_version),
        trt_utils.version_tuple_to_string(linked_version))
    raise RuntimeError("Incompatible TensorRT major version")

elif loaded_version != linked_version:
    logging.info(
        "Loaded TensorRT %s and linked TensorFlow against TensorRT %s. This is "
        "supported because TensorRT minor/patch upgrades are backward "
        "compatible.", trt_utils.version_tuple_to_string(loaded_version),
        trt_utils.version_tuple_to_string(linked_version))
