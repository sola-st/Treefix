# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
"""Initializes the `step_context` argument for a `step_fn` invocation.

      Args:
        session: An instance of `tf.compat.v1.Session`.
        run_with_hooks_fn: A function for running fetches and hooks.
      """
self._session = session
self._run_with_hooks_fn = run_with_hooks_fn
