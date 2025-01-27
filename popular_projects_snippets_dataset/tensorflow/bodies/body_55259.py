# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
c = a + b * 2  # Create some ops to have nodes in the body
print(c)  # Using 'print' to make lint happy
