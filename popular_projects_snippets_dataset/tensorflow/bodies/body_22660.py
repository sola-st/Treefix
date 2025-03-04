# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla.py
"""Builds an operator that compiles and runs `computation` with XLA.

  NOTE: In eager mode, `computation` will have `@tf.function` semantics.

  Args:
    computation: A Python function that builds a computation to apply to the
      input. If the function takes n inputs, 'inputs' should be a list of n
      `Tensor`s.

      `computation` may return a list of `Tensor`s and `Operation`s.
      `Tensor`s must come before `Operation`s in the returned list.

      All `Operation`s returned from `computation` will be executed when
      evaluating any of the returned output tensors.
    inputs: A list of inputs or `None` (equivalent to an empty list). Each input
      can be a nested structure containing values that can be converted to
      `Tensor`s. Note that passing an N-dimension list of compatible values will
      result in an N-dimension list of scalar `Tensor`s rather than a single
      Rank-N `Tensor`. If you need a different behavior, convert parts of
      `inputs` to `Tensor`s with `tf.convert_to_tensor`.

  Returns:
    List of `Tensor`s corresponding to the `Tensor`s from
      the output of `computation` i.e. the same return value as if
      computation(*inputs) is called directly, with the following exceptions:
      * None output: a NoOp would be returned with a control dependency on
         `computation`.
      * Single value output: a tuple containing the value would be returned.
      * Operation-only outputs: a NoOp would be returned with a control
      dependency on `computation`.
      TODO(b/121383831): Investigate into removing these special cases.

  Raises:
    RuntimeError: When eager execution is enabled.

  Known issues:
    When a tf.random operation is built with XLA, the implementation doesn't
      pass the user provided seed to the XLA compiler. As such, the XLA compiler
      generates a random number and uses it as a seed when compiling the
      operation. This implementation causes a violation of the Tensorflow
      defined semantics in two aspects. First, changing the value of the user
      defined seed doesn't change the numbers generated by the operation.
      Second, when a seed is not specified, running the program multiple times
      will generate the same numbers.
  """
if context.executing_eagerly():

    @def_function.function
    def xla_compile_wrapper():
        exit(_compile_internal(computation, inputs))

    exit(xla_compile_wrapper())

exit(_compile_internal(computation, inputs))
