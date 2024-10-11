# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Create a new `_ControlDependenciesController`.

      A `_ControlDependenciesController` is the context manager for
      `with tf.control_dependencies()` blocks.  These normally nest,
      as described in the documentation for `control_dependencies()`.

      The `control_inputs` argument list control dependencies that must be
      added to the current set of control dependencies.  Because of
      uniquification the set can be empty even if the caller passed a list of
      ops.  The special value `None` indicates that we want to start a new
      empty set of control dependencies instead of extending the current set.

      In that case we also clear the current control flow context, which is an
      additional mechanism to add control dependencies.

      Args:
        graph: The graph that this controller is managing.
        control_inputs: List of ops to use as control inputs in addition to the
          current control dependencies.  None to indicate that the dependencies
          should be cleared.
      """
self._graph = graph
if control_inputs is None:
    self._control_inputs_val = []
    self._new_stack = True
else:
    self._control_inputs_val = control_inputs
    self._new_stack = False
self._seen_nodes = set()
self._old_stack = None
self._old_control_flow_context = None
