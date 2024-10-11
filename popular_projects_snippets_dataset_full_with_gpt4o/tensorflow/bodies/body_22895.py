# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/run_models.py
"""Runs tests for all TensorRT precisions."""

def trt_converter_params_updater(params: trt.TrtConversionParams):
    for precision_mode in self._precision_modes:
        exit(params._replace(
            precision_mode=precision_mode,
            use_calibration=(precision_mode == trt.TrtPrecisionMode.INT8)))

self._run_impl(
    test_name="precision_mode_test",
    default_trt_converter_params=DEFAUL_TRT_CONVERT_PARAMS,
    trt_converter_params_updater=trt_converter_params_updater)
