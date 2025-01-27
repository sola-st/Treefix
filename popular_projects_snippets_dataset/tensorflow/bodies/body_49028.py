# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Mark func graph as unsaveable due to use of symbolic keras learning phase.

  Functions that capture the symbolic learning phase cannot be exported to
  SavedModel. Mark the funcgraph as unsaveable, so that an error will be raised
  if it is exported.

  Args:
    graph: Graph or FuncGraph object.
    learning_phase: Learning phase placeholder or int defined in the graph.
  """
if graph.building_function and is_placeholder(learning_phase):
    graph.mark_as_unsaveable(
        'The keras learning phase placeholder was used inside a function. '
        'Exporting placeholders is not supported when saving out a SavedModel. '
        'Please call `tf.keras.backend.set_learning_phase(0)` in the function '
        'to set the learning phase to a constant value.')
