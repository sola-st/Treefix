# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/exceptions.py
"""Overload of assert_stmt that stages a TF Assert.

  This implementation deviates from Python semantics as follows:
    (1) the assertion is verified regardless of the state of __debug__
    (2) on assertion failure, the graph execution will fail with
        tensorflow.errors.ValueError, rather than AssertionError.

  Args:
    expression1: tensorflow.Tensor, must evaluate to a tf.bool scalar
    expression2: Callable[[], Union[tensorflow.Tensor, List[tensorflow.Tensor]]]

  Returns:
    tensorflow.Operation
  """
expression2_tensors = expression2()
if not isinstance(expression2_tensors, list):
    expression2_tensors = [expression2_tensors]
exit(control_flow_ops.Assert(expression1, expression2_tensors))
