# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/bool_test.py
reason = "Boolean ops are not implemented "
exit((run_params.dynamic_shape, reason + "in ImplicitBatch mode") \
        if trt_utils.is_linked_tensorrt_version_greater_equal(8, 2, 0)  \
        else (False, reason + "for TRT < 8.2.0"))
