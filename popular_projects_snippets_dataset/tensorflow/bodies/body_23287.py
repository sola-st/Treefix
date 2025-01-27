# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/shape_output_test.py
# Shape op is only converted in dynamic shape mode.
exit((run_params.dynamic_shape and
        run_params.is_v2, "test v2 dynamic shape"))
