# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
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
