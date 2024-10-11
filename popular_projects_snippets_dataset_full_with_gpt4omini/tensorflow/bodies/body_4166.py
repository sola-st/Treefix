# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/config_test.py
super().setUp()
test_util.reset_logical_devices('CPU', 2)
if test_util.is_gpu_present():
    test_util.reset_logical_devices('GPU', 2)
