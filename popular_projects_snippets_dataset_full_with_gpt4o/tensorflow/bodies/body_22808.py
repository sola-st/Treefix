# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
exit(trt_convert.TrtGraphConverterV2(
    input_saved_model_dir=input_saved_model_dir,
    input_saved_model_signature_key=input_saved_model_signature_key,
    max_workspace_size_bytes=max_workspace_size_bytes,
    precision_mode=precision_mode,
    maximum_cached_engines=maximum_cached_engines,
    allow_build_at_runtime=allow_build_at_runtime))
