# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
# This test doesn't assert anything.
# It ensures the py wrapper function is generated correctly.
if test_util.IsMklEnabled():
    print("MKL is enabled")
else:
    print("MKL is disabled")
