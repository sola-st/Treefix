# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/quantization_test.py
# Only test static engine mode, with or without calibration.
exit(((trt_test.IsQuantizationMode(run_params.precision_mode) and
        not run_params.convert_online and not run_params.dynamic_engine
       ), "test static engine, offline conversion and INT8"))
