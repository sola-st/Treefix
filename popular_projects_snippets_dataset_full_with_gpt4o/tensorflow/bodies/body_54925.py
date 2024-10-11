# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks.py
r"""Add a thread-local callback that intercepts op execution and op creation.

  The `callback_fn` will be invoked immediately after any of the three types
  of events:
    - The execution of an TensorFlow operation ("op" for short hereafter)
      under eager mode,
    - The execution of a FuncGraph under eager mode,
    - The creation of an op during graph construction (e.g., in
      @tf.function-decorated Python functions).

  Known limitations:
    1. Under graph mode, overriding the output tensors of control-flow ops,
       including "If", "StatelessIf" and "While", may cause errors
       (b/139668453). Overriding other tensors in a graph consisting of such
       control-flow ops is okay.
    2. Under eager mode, calling eager ops from the callback function itself
       may lead to recursion stack overflow. This can be prevented by
       returning from the callback function immediately on encountering the
       op type involved (b/140334369).

  Args:
    callback_fn: A callback_fn that has the following signature:
      def callback_fn(op_type,
                      inputs,
                      attrs,
                      outputs,
                      op_name=None,
                      graph=None):
        # op_type: The type of the op, as a string. E.g., "MatMul".
        #          For the special case of FuncGraph execution, op_type
        #          takes the name of the graph name, e.g.,
        #          "__inference_my_func_24".
        # inputs: (`tuple` of `Tensor`s) Input tensors to the op or the
        #         FuncGraph.
        #         - In eager execution, these are `EagerTensor`s.
        #         - In graph construction, these are non-eager `Tensor`s
        #           that form the inputs to the just-created op.
        # attrs: The attributes of the op or FuncGraph of which the execution
        #        or creation caused the current invocation of the callback.
        #        This is applicable to both eager- and graph-based execution,
        #        as well as graph construction.
        #        This is a tuple of alternating attribute keys and attribute
        #        values. E.g., `('adjoint_a', False, 'adjoint_b', False)`.
        # outputs: (`tuple of `Tensor`s) Output tensors from the op or
        #          FuncGraph.
        #          In eager execution, these are `EagerTensor`s.
        #          In graph construction, these are non-eager `Tensor`s that
        #          are the outputs of the just-created op.
        # op_name: Name of the op.
        #          - If the current invocation of the callback is due to the
        #            eager execution of an op or FuncGraph, this will be
        #            `None`, as op names are meaningless in eager execution.
        #          - In graph construction, this is the name of the op, e.g.,
        #            "MatMul_2".
        # graph: The graph that the op belongs to (if any).
        #        - In eager execution of an op or FuncGraph, this is `None`.
        #        - In graph construction, this is the op's enclosing graph
        #          as a `tf.Graph` object.
        #
        # Return values:
        #   This callback function is expected to return `None` or
        #   a `list` or `tuple` of `Tensor`s with its length matching
        #   `len(outputs)`, in the order that corresponds to that of the
        #   `outputs` argument.
        #   If the return value is `None`, downstream execution or graph
        #   construction will be unaffected.
        #   However, if the return value is a `list` or `tuple` of `Tensor`s,
        #   - In eager execution, these returned `Tensor`s should be
        #     `EagerTensor`s. Their values will replace the original values of
        #     `outputs` for downstream eager execution. (*Not implemented yet*).
        #   - In graph construction, these returned `Tensor`s should be
        #     non-eager `Tensor`s. Their values will replace the original
        #     `outputs` for downstream graph construction.

  Raises:
    ValueEror: If `callback_fn` is `None` or not callable.
  """
# TODO(b/139668041): Implement support for overriding `EagerTensor`s from
# callback.
if callback_fn is None:
    raise ValueError("Passed callback function cannot be None.")
if not callable(callback_fn):
    raise ValueError(
        "Callback function passed to op_callback() is expected to be callable, "
        f"but got {callback_fn} of type {type(callback_fn)}.")
ctx = context.context()
ctx.add_op_callback(callback_fn)
if ctx.executing_eagerly():
    # Monkey-patch `execute.execute()`.
    execute.execute = execute.execute_with_callbacks
