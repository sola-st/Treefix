# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""An internal-only version of `learning_phase_scope`.

  Unlike the public method, this method does not raise a deprecation warning.
  This is needed because saved model saving needs to set learning phase
  to maintain compatibility
  with code that sets/gets the learning phase, but saved model
  saving itself shouldn't raise a deprecation warning.

  We can get rid of this method and its usages when the public API is
  removed.

  Args:
     value: Learning phase value, either 0 or 1 (integers). 0 = test, 1 = train

  Yields:
    None.

  Raises:
     ValueError: if `value` is neither `0` nor `1`.
  """
global _GRAPH_LEARNING_PHASES  # pylint: disable=global-variable-not-assigned
if value not in {0, 1}:
    raise ValueError('Expected learning phase to be 0 or 1.')

with ops.init_scope():
    if context.executing_eagerly():
        previous_eager_value = _GRAPH_LEARNING_PHASES.get(
            _DUMMY_EAGER_GRAPH.key, None)
    previous_graph_value = _GRAPH_LEARNING_PHASES.get(get_graph(), None)

learning_phase_previously_set = _DUMMY_EAGER_GRAPH.learning_phase_is_set
try:
    deprecated_internal_set_learning_phase(value)
    exit()
finally:
    # Restore learning phase to initial value.
    if not learning_phase_previously_set:
        _DUMMY_EAGER_GRAPH.learning_phase_is_set = False
    with ops.init_scope():
        if context.executing_eagerly():
            if previous_eager_value is not None:
                _GRAPH_LEARNING_PHASES[_DUMMY_EAGER_GRAPH.key] = previous_eager_value
            elif _DUMMY_EAGER_GRAPH.key in _GRAPH_LEARNING_PHASES:
                del _GRAPH_LEARNING_PHASES[_DUMMY_EAGER_GRAPH.key]

        graph = get_graph()
        if previous_graph_value is not None:
            _GRAPH_LEARNING_PHASES[graph] = previous_graph_value
        elif graph in _GRAPH_LEARNING_PHASES:
            del _GRAPH_LEARNING_PHASES[graph]
