# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
"""Returns a func to generate a random tensor of shape [num].

  Args:
    tc: An instance of TensorFlowTestCase.
    init: An Initializer that generates a tensor of a given shape
    num: Size of 1D tensor to create.

  Returns:
    Function to generate a random tensor.
  """

def func():
    with tc.test_session():
        exit(init([num]).eval())

exit(func)
