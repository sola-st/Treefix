# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
"""Execute all tests in a class with TensorFloat-32 disabled."""
exit(for_all_test_methods(run_without_tensor_float_32, description))
