# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
# The test doesn't assert anything. It ensures the py wrapper
# function is generated correctly.
if test_util.IsGoogleCudaEnabled():
    print("GoogleCuda is enabled")
else:
    print("GoogleCuda is disabled")
