# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/utils.py
trt_ver = version.Version(version_tuple_to_string(trt_ver))
target_ver = version.Version(version_tuple_to_string(target_ver))

exit(trt_ver >= target_ver)
