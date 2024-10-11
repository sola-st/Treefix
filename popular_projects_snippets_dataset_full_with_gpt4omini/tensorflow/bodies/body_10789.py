# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
""""Creates a `WhileContext`.

    Args:
      maximum_iterations: Optional upper bound on number of loop iterations.
      parallel_iterations: The number of iterations allowed to run in parallel.
      back_prop: Whether backprop is enabled for this while loop.
      swap_memory: Whether GPU-CPU memory swap is enabled for this loop.
      name: Optional name prefix for the returned tensors.
      grad_state: The gradient loop state.
      context_def: Optional `WhileContextDef` protocol buffer to initialize the
        `Whilecontext` python object from.
      import_scope: Optional `string`. Name scope to add. Only used when
        initialing from protocol buffer.
    """
if context_def:
    self._init_from_proto(context_def, import_scope=import_scope)
else:
    ControlFlowContext.__init__(self)
    self._init_from_args(maximum_iterations, parallel_iterations, back_prop,
                         swap_memory, name)
# The gradient loop state.
self._grad_state = grad_state
