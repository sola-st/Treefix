# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Internal scope that sets the learning phase in eager / tf.function only.

  Args:
      value: Learning phase value, either 0 or 1 (integers).
             0 = test, 1 = train

  Yields:
    None.

  Raises:
     ValueError: if `value` is neither `0` nor `1`.
  """
global _GRAPH_LEARNING_PHASES  # pylint: disable=global-variable-not-assigned
assert value in {0, 1}
assert ops.executing_eagerly_outside_functions()
global_learning_phase_was_set = global_learning_phase_is_set()
if global_learning_phase_was_set:
    previous_value = learning_phase()
try:
    _GRAPH_LEARNING_PHASES[_DUMMY_EAGER_GRAPH.key] = value
    exit()
finally:
    # Restore learning phase to initial value or unset.
    if global_learning_phase_was_set:
        _GRAPH_LEARNING_PHASES[_DUMMY_EAGER_GRAPH.key] = previous_value
    else:
        del _GRAPH_LEARNING_PHASES[_DUMMY_EAGER_GRAPH.key]
