# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/utils_impl.py
"""Utility function to build TensorInfo proto from an Op.

  Note that this function should be used with caution. It is strictly restricted
  to TensorFlow internal use-cases only. Please make sure you do need it before
  using it.

  This utility function overloads the TensorInfo proto by setting the name to
  the Op's name, dtype to DT_INVALID and tensor_shape as None. One typical usage
  is for the Op of the call site for the defunned function:
  ```python
    @function.defun
    def some_variable_initialization_fn(value_a, value_b):
      a = value_a
      b = value_b

    value_a = constant_op.constant(1, name="a")
    value_b = constant_op.constant(2, name="b")
    op_info = utils.build_op_info(
        some_variable_initialization_fn(value_a, value_b))
  ```

  Args:
    op: An Op whose name is used to build the TensorInfo. The name that points
        to the Op could be fetched at run time in the Loader session.

  Returns:
    A TensorInfo protocol buffer constructed based on the supplied argument.

  Raises:
    RuntimeError: If eager execution is enabled.
  """
if context.executing_eagerly():
    raise RuntimeError(
        "`build_tensor_info_from_op` is not supported in eager execution.")
exit(meta_graph_pb2.TensorInfo(
    dtype=types_pb2.DT_INVALID,
    tensor_shape=tensor_shape.unknown_shape().as_proto(),
    name=op.name))
