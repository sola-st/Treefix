# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/shape_output_test.py
# We cannot calibrate without bulding the engine, we turn of INT8 test.
exit((run_params.dynamic_shape and
        run_params.precision_mode != "INT8", "no calibration dynamic shape"))
