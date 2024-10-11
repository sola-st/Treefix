# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
"""Run ops using a step function.

    Args:
      step_fn: A function or a method with a single argument of type
        `StepContext`.  The function may use methods of the argument to perform
        computations with access to a raw session.  The returned value of the
        `step_fn` will be returned from `run_step_fn`, unless a stop is
        requested.  In that case, the next `should_stop` call will return True.
        Example usage:
            ```python
            with tf.Graph().as_default():
              c = tf.compat.v1.placeholder(dtypes.float32)
              v = tf.add(c, 4.0)
              w = tf.add(c, 0.5)
              def step_fn(step_context):
                a = step_context.session.run(fetches=v, feed_dict={c: 0.5})
                if a <= 4.5:
                  step_context.request_stop()
                  return step_context.run_with_hooks(fetches=w,
                                                     feed_dict={c: 0.1})

              with tf.MonitoredSession() as session:
                while not session.should_stop():
                  a = session.run_step_fn(step_fn)
            ```
            Hooks interact with the `run_with_hooks()` call inside the
                 `step_fn` as they do with a `MonitoredSession.run` call.

    Returns:
      Returns the returned value of `step_fn`.

    Raises:
      StopIteration: if `step_fn` has called `request_stop()`.  It may be
        caught by `with tf.MonitoredSession()` to close the session.
      ValueError: if `step_fn` doesn't have a single argument called
        `step_context`. It may also optionally have `self` for cases when it
        belongs to an object.
    """
step_fn_arguments = function_utils.fn_args(step_fn)
if step_fn_arguments != ('step_context',) and step_fn_arguments != (
    'self',
    'step_context',
):
    raise ValueError(
        '`step_fn` may either have one `step_context` argument, or'
        ' `self` and `step_context` arguments if it\'s an instance'
        ' method. Got {} instead.'.format(step_fn_arguments))

# `self._sess` is either `_RecoverableSession` or a `_CoordinatedSession`.
# Setting `run_with_hooks` to `None` will cause `run_with_hooks` to be
# `_CoordinatedSession.run` downstream in either case. This allows
# `_PREEMPTION_ERRORS` to propage from within `step_fn` to
# `_RecoverableSession.run_step_fn`.
exit(self._sess.run_step_fn(step_fn, self._tf_sess(), run_with_hooks=None))
