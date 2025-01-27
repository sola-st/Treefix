# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""A deprecated internal implementation of set_learning_phase.

  This method is an internal-only version of `set_learning_phase` that
  does not raise a deprecation error. It is required because
  saved_model needs to keep working with user code that uses the deprecated
  learning phase methods until those APIs are fully removed from the public API.

  Specifically SavedModel saving needs to make sure the learning phase is 0
  during tracing even if users overwrote it to a different value.

  But, we don't want to raise deprecation warnings for users when savedmodel
  sets learning phase just for compatibility with code that relied on
  explicitly setting the learning phase for other values.

  Args:
      value: Learning phase value, either 0 or 1 (integers). 0 = test, 1 = train

  Raises:
      ValueError: if `value` is neither `0` nor `1`.
  """
global _GRAPH_LEARNING_PHASES  # pylint: disable=global-variable-not-assigned
if value not in {0, 1}:
    raise ValueError('Expected learning phase to be 0 or 1.')
with ops.init_scope():
    if context.executing_eagerly():
        # In an eager context, the learning phase values applies to both the eager
        # context and the internal Keras graph.
        _DUMMY_EAGER_GRAPH.learning_phase_is_set = True
        _GRAPH_LEARNING_PHASES[_DUMMY_EAGER_GRAPH.key] = value
    _GRAPH_LEARNING_PHASES[get_graph()] = value
