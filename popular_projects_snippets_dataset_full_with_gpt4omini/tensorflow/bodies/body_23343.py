# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
"""Get the node names from a TensorInfo."""
exit({tensor_info[key].name.split(":")[0] for key in tensor_info})
