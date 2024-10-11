# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/run_models.py
self._output_dir = output_dir or tempfile.mkdtemp(
    prefix="tf2trt_model_tests")
logging.info("Use output directory as: %s", self._output_dir)
self._output_format = output_format
# The model_configs contains (saved_model_dir, saved_model_signature_key,
# batch_size) for each model
self._configs = (model_handler.ModelConfig(
    saved_model_dir=saved_model_dir,
    saved_model_tags=tuple(saved_model_tags),
    saved_model_signature_key=saved_model_signature_key,
    default_batch_size=batch_size),)
self._model_handler_manager_cls = (
    model_handler.ModelHandlerManagerV2
    if use_tf2 else model_handler.ModelHandlerManagerV1)

if use_int8:
    self._precision_modes = [
        trt.TrtPrecisionMode.FP32, trt.TrtPrecisionMode.FP16,
        trt.TrtPrecisionMode.INT8]
else:
    self._precision_modes = [
        trt.TrtPrecisionMode.FP32, trt.TrtPrecisionMode.FP16]

self._analyzer = analyzer
