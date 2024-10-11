# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_run.py
ctx = context.context()
eager_context_state = ctx._thread_local_data  # pylint: disable=protected-access
eager_context_state.op_callbacks = self._eager_context_op_callbacks
