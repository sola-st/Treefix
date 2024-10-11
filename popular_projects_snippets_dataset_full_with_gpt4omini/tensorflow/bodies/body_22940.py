# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
exit(trt.TrtGraphConverterV2(
    input_saved_model_dir=self.model_config.saved_model_dir,
    input_saved_model_tags=self.model_config.saved_model_tags,
    input_saved_model_signature_key=(
        self.model_config.saved_model_signature_key),
    **trt_convert_params._asdict()))
