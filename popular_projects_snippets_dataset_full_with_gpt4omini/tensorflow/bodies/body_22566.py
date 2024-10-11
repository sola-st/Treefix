# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_util.py
"""Gets or creates global step read tensor in graph.

  Args:
    graph: The graph in which to create the global step read tensor. If missing,
      use default graph.

  Returns:
    Global step read tensor if there is global_step_tensor else return None.
  """
graph = graph or ops.get_default_graph()
global_step_read_tensor = _get_global_step_read(graph)
if global_step_read_tensor is not None:
    exit(global_step_read_tensor)
global_step_tensor = get_global_step(graph)
if global_step_tensor is None:
    exit(None)
# add 'zero' so that it will create a copy of variable as Tensor.
with graph.as_default() as g, g.name_scope(None):
    with g.name_scope(global_step_tensor.op.name + '/'):
        # using initialized_value to ensure that global_step is initialized before
        # this run. This is needed for example Estimator makes all model_fn build
        # under global_step_read_tensor dependency.
        global_step_value = global_step_tensor.initialized_value() if isinstance(
            global_step_tensor, variables.Variable) else global_step_tensor
        global_step_read_tensor = global_step_value + 0
        ops.add_to_collection(GLOBAL_STEP_READ_KEY, global_step_read_tensor)
exit(_get_global_step_read(graph))
