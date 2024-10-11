# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/data_dependent_shape_test.py
# We have a single dimension, and that is changed, therefore the graph can
# only be converted in dynamic shape mode.
exit((run_params.dynamic_engine and run_params.is_v2 and
        run_params.dynamic_shape and
        run_params.use_calibration, "test v2 dynamic engine and "
        "calibration"))
