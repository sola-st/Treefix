# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util_v2.py
"""Fix higher-order tape gradients by wrapping `make_op` in a function.

  Args:
    make_op: A function that takes a list of inputs and returns a list of output
      tensors. This function should set any handle data relevant to its outputs
      before returning.
    inputs: A list of tensors to check for tape gradients and pass to
      `make_op`. These should include all tensors used in `make_op`.

  Returns:
    Tensors corresponding to `make_op`'s output.
  """
# GradientTapes created inside a function currently don't work well with
# un-wrapped control flow ops in that same function. Wrapping in an extra
# layer of intermediate function means we run extra logic in the function
# gradient code to record the correct intermediates on the tape.
#
# The function attribute inputs to control flow ops are not hashable, so we
# pass everything as a capture to bypass defun's caching.
if (gradients_util.PossibleTapeGradientTypes(inputs)
    == gradients_util.POSSIBLE_GRADIENT_TYPES_HIGHER_ORDER
    # We only need one function between the tape and the op; if we've already
    # wrapped once, we stop wrapping to avoid infinite recursion.
    and not (ops.get_default_graph().building_function
             and "cflow_gradient_wrapper" in ops.get_default_graph().name)):
    results = function.defun_with_attributes(
        make_op,
        autograph=False,
        attributes=dict(func_name="cflow_gradient_wrapper"))(inputs)
    exit(results)
else:
    exit(make_op(inputs))
