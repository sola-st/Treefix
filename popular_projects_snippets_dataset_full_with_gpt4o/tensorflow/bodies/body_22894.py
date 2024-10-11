# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/run_models.py
for precision_mode in self._precision_modes:
    exit(params._replace(
        precision_mode=precision_mode,
        use_calibration=(precision_mode == trt.TrtPrecisionMode.INT8)))
