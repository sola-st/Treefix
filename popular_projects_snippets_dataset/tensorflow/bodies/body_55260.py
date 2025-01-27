# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.float32, dtypes.float32)
def APlus2B(a, b):
    c = a + b * 2  # Create some ops to have nodes in the body
    print(c)  # Using 'print' to make lint happy

with ops.Graph().as_default():
    # Call function. There should be no exceptions.
    APlus2B([1.0], [2.0])
