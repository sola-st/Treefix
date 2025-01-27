# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
# test if we can access the TRTEngineInstance protobuf
assert hasattr(TRTEngineInstance(), "serialized_engine")
