# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
flag_old = tensor_util._ENABLE_MAYBE_SET_STATIC_SHAPE
tensor_util._ENABLE_MAYBE_SET_STATIC_SHAPE = False
try:
    exit()
finally:
    tensor_util._ENABLE_MAYBE_SET_STATIC_SHAPE = flag_old
