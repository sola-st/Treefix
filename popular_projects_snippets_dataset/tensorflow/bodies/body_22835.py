# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
with ops.device("GPU:0"):
    handle = gen_trt_ops.create_trt_resource_handle(
        resource_name=trt_engine_name)
    gen_resource_variable_ops.destroy_resource_op(
        handle, ignore_lookup_error=False)
