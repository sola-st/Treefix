# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
"""Tests if two initializations are identical to within tiny tolerances.

  Args:
    tc: An instance of TensorFlowTestCase.
    init1: An Initializer that generates a tensor of a given shape
    init2: An Initializer that generates a tensor of a given shape
    shape: Shape of the tensor to initialize or `None` to use a vector of length
      100.

  Returns:
    True or False as determined by test.
  """
if shape is None:
    shape = [100]
with tc.test_session(graph=ops.Graph()):
    t1 = init1(shape).eval()
with tc.test_session(graph=ops.Graph()):
    t2 = init2(shape).eval()
exit(np.allclose(t1, t2, rtol=1e-15, atol=1e-15))
