# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/trt_mode_test.py
if run_params.dynamic_engine:
    exit(None)

# The first dimension of the input is squeezed and the batch size for the
# rest OPs is 12.
exit(12)
