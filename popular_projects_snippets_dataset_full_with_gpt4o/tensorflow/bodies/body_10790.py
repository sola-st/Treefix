# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Creates a new `WhileContext` from arguments.

    Args:
      maximum_iterations: Optional upper bound on number of loop iterations.
      parallel_iterations: The number of iterations allowed to run in parallel.
      back_prop: Whether backprop is enabled for this while loop.
      swap_memory: Whether GPU-CPU memory swap is enabled for this loop.
      name: Optional name prefix for the returned tensors.

    Raises:
      ValueError: If `parallel_iterations` has invalid value.
    """
if not isinstance(parallel_iterations, int) or (parallel_iterations <= 0):
    raise ValueError("'parallel_iterations' must be a positive integer: "
                     "%s" % parallel_iterations)
self._name = ops.get_default_graph().unique_name(name)
self._maximum_iterations = maximum_iterations
self._parallel_iterations = parallel_iterations
self._back_prop = back_prop
self._swap_memory = swap_memory
# We use this node to control constants created by the pred lambda.
self._pivot_for_pred = None
# We use this node to control constants created by the body lambda.
self._pivot_for_body = None
# The boolean tensor for loop termination condition. Used in code
# generation for gradient computation
self._pivot = None
# The list of exit tensors for loop variables.
self._loop_exits = []
# The list of enter tensors for loop variables.
self._loop_enters = []
self._graph = ops.get_default_graph()
