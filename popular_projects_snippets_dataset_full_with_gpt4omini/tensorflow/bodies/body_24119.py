# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework.py
"""Constructor of `BaseDebugWrapperSession`.

    Args:
      sess: An (unwrapped) TensorFlow session instance. It should be a subtype
        of `BaseSession` or `tf.MonitoredSession`.
      thread_name_filter: Regular-expression filter (allowlist) for name(s) of
        thread(s) on which the wrapper session will be active. This regular
        expression is used in a start-anchored fashion on the thread name, i.e.,
        by applying the `match` method of the compiled pattern. The default
        `None` means that the wrapper session will be active on all threads.
        E.g., r"MainThread$", r"QueueRunnerThread.*".
      pass_through_operrors: If True, all captured OpErrors will be
        propagated.  By default this captures all OpErrors.

    Raises:
      ValueError: On invalid `OnSessionInitAction` value.
      NotImplementedError: If a non-DirectSession sess object is received.
    """

_check_type(sess, (session.BaseSession, monitored_session.MonitoredSession))

# The session being wrapped.
self._sess = sess
self._thread_name_filter_pattern = (re.compile(thread_name_filter)
                                    if thread_name_filter else None)
# TODO(cais/kstevens): Unittest this pass through feature.
self._pass_through_operrors = pass_through_operrors

# Keeps track of number of run calls that have been performed on this
# debug-wrapper session. The count can be used for purposes such as
# displaying the state of the Session in a UI and determining a run
# number-dependent debug URL.
self._run_call_count = 0

# Invoke on-session-init callback.
response = self.on_session_init(OnSessionInitRequest(self._sess))
_check_type(response, OnSessionInitResponse)

if response.action == OnSessionInitAction.PROCEED:
    pass
elif response.action == OnSessionInitAction.REMOTE_INSTR_LOOP:
    # TODO(cais): Implement REMOTE_INSTR_LOOP
    raise NotImplementedError(
        "OnSessionInitAction REMOTE_INSTR_LOOP has not been "
        "implemented.")
else:
    raise ValueError(
        "Invalid OnSessionInitAction value: %s" % response.action)

self._default_session_context_manager = None

# A cache for callables created from CallableOptions.
self._cached_callables_from_options = {}
