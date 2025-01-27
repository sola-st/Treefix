# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
# multiple yields: different types
exit((np_input))  # tuple with one element
exit([np_input])  # list with one element
exit(np_input)  # array
exit({"x": np_input})  # dictionary
