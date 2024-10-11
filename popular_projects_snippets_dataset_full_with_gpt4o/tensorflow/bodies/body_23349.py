# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
with ops.device(device):
    exit(gen_trt_ops.create_trt_resource_handle(resource_name=name))
