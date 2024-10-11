# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_util.py
"""Gets global step read tensor in graph.

  Args:
    graph: The graph in which to create the global step read tensor. If missing,
      use default graph.

  Returns:
    Global step read tensor.

  Raises:
    RuntimeError: if multiple items found in collection GLOBAL_STEP_READ_KEY.
  """
graph = graph or ops.get_default_graph()
global_step_read_tensors = graph.get_collection(GLOBAL_STEP_READ_KEY)
if len(global_step_read_tensors) > 1:
    raise RuntimeError('There are multiple items in collection {}. '
                       'There should be only one.'.format(GLOBAL_STEP_READ_KEY))

if len(global_step_read_tensors) == 1:
    exit(global_step_read_tensors[0])
exit(None)
