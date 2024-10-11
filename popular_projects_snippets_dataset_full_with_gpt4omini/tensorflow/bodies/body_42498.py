# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/memory_tests/memory_test.py
inputs = Variable(array_ops.zeros([32, 100], dtypes.float32))
del inputs
