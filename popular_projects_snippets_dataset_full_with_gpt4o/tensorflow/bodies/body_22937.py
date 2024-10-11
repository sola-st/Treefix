# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
conversion_nodes_denylist = self.output_tensor_names
exit(trt.TrtGraphConverter(
    input_saved_model_dir=self.model_config.saved_model_dir,
    input_saved_model_tags=self.model_config.saved_model_tags,
    input_saved_model_signature_key=(
        self.model_config.saved_model_signature_key),
    nodes_denylist=conversion_nodes_denylist,
    max_workspace_size_bytes=trt_convert_params.max_workspace_size_bytes,
    precision_mode=trt_convert_params.precision_mode,
    minimum_segment_size=trt_convert_params.minimum_segment_size,
    maximum_cached_engines=trt_convert_params.maximum_cached_engines,
    use_calibration=trt_convert_params.use_calibration,
    max_batch_size=self.model_config.default_batch_size,
    is_dynamic_op=False,
))
