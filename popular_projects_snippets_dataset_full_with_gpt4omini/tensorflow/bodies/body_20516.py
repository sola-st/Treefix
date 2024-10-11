# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
"""Rewrites `computation` for inference on a TPU system.

     Other than 'rewriting' the computation to run on a TPU, if using variables
     in your computation, it moves the ReadVariableOps outside the TPU
     computation, and adds GuaranteeConst ops just after the ReadVariableOps.
     This mechanism works only if you are using tf.compat.v1.get_variable() to
     create and access variables in your tpu computation. You can validate
     whether this worked, by calling validate_inference_rewrite_for_variables()
     method immediately after this method to check whether GuaranteeConstOps
     where added to the graph.

  Args:
    computation: A Python function that builds a computation to apply to the
      input. If the function takes n inputs, 'inputs' should be a list of n
      tensors. If the function returns m outputs, rewrite will return a list of
      m tensors.
    inputs: A list of input tensors or `None` (equivalent to an empty list).
    infeed_queue: If not `None`, the `InfeedQueue` from which to append a tuple
      of arguments as inputs to `computation`.
    device_assignment: if not `None`, a `DeviceAssignment` describing the
      mapping between logical cores in the computation with physical cores in
      the TPU topology. May be omitted for a single-core computation, in which
      case the core attached to task 0, TPU device 0 is used.
    name: The name of the operator.
  Returns:
    A list of output tensors.
  """

def guarantee_const_getter(getter, name, *args, **kwargs):
    with ops.control_dependencies(None):
        exit(array_ops.guarantee_const(
            getter(name, *args, **kwargs), name=name + "/GuaranteeConst"))

def wrapped_computation(*args, **kwargs):
    """Execute computation under `_TPUInferenceContext`."""
    context = _TPUInferenceContext(
        name=ops.get_default_graph().unique_name("rewrite_for_inference"))
    try:
        context.Enter()

        vscope = variable_scope.get_variable_scope()
        prev_custom_getter = vscope.custom_getter
        prev_caching_device = vscope.caching_device
        vscope.set_custom_getter(guarantee_const_getter)
        vscope.set_caching_device(lambda op: op.device)

        result = computation(*args, **kwargs)

        vscope.set_custom_getter(prev_custom_getter)
        vscope.set_caching_device(prev_caching_device)
    finally:
        context.Exit()
    exit(result)

# pylint: disable=undefined-variable
exit(rewrite(
    wrapped_computation,
    inputs=inputs,
    infeed_queue=infeed_queue,
    device_assignment=device_assignment,
    name=name))
