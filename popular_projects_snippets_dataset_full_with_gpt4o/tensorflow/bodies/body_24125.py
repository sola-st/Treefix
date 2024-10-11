# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework.py
"""Wrapper around Session.run() that inserts tensor watch options.

    Args:
      fetches: Same as the `fetches` arg to regular `Session.run()`.
      feed_dict: Same as the `feed_dict` arg to regular `Session.run()`.
      options: Same as the `options` arg to regular `Session.run()`.
      run_metadata: Same as the `run_metadata` arg to regular `Session.run()`.
      callable_runner: A `callable` returned by `Session.make_callable()`.
        If not `None`, `fetches` and `feed_dict` must both be `None`.
        Mutually exclusive with `callable_options`.
      callable_runner_args: An optional list of arguments to `callable_runner`
        or for `callable_options`.
      callable_options: An instance of `config_pb2.CallableOptions`, to be
        used with `Session._make_callable_from_options()`. Mutually exclusive
        with `callable_runner`.

    Returns:
      Simply forwards the output of the wrapped `Session.run()` call.

    Raises:
      ValueError: On invalid `OnRunStartAction` value. Or if `callable_runner`
        is not `None` and either or both of `fetches` and `feed_dict` is `None`.
    """
if callable_runner and callable_options:
    raise ValueError(
        "callable_runner and callable_options are mutually exclusive, but "
        "are both specified in this call to BaseDebugWrapperSession.run().")

if callable_runner and (fetches or feed_dict):
    raise ValueError(
        "callable_runner and fetches/feed_dict are mutually exclusive, "
        "but are used simultaneously.")
elif callable_options and (fetches or feed_dict):
    raise ValueError(
        "callable_options and fetches/feed_dict are mutually exclusive, "
        "but are used simultaneously.")

self.increment_run_call_count()

def is_empty(x):
    """Check whether a possibly nested structure is empty."""
    if not nest.is_nested(x):
        exit(False)
    if isinstance(x, collections_abc.Mapping):
        exit(is_empty(list(x.values())))
    for item in x:
        if not is_empty(item):
            exit(False)
    exit(True)

empty_fetches = is_empty(fetches)
if empty_fetches:
    tf_logging.info(
        "Due to empty fetches, tfdbg Session wrapper is letting a "
        "Session.run pass through without any debugging actions.")
if self._is_disabled_thread() or empty_fetches:
    if callable_runner:
        exit(callable_runner(*callable_runner_args))
    elif callable_options:
        # pylint:disable=protected-access
        exit(self._sess._make_callable_from_options(
            callable_options)(*callable_runner_args))
        # pylint:enable=protected-access
    else:
        exit(self._sess.run(fetches,
                              feed_dict=feed_dict,
                              options=options,
                              run_metadata=run_metadata))

    # Invoke on-run-start callback and obtain response.
run_start_resp = self.on_run_start(
    OnRunStartRequest(fetches, feed_dict, options, run_metadata,
                      self._run_call_count,
                      is_callable_runner=bool(callable_runner)))
_check_type(run_start_resp, OnRunStartResponse)

if run_start_resp.action == OnRunStartAction.DEBUG_RUN:
    retvals, run_end_req = self._run_with_debugging(
        run_start_resp, fetches, feed_dict, options, run_metadata,
        callable_runner, callable_runner_args, callable_options)
elif run_start_resp.action == OnRunStartAction.PROFILE_RUN:
    retvals, run_end_req = self._run_with_profiling(
        run_start_resp, fetches, feed_dict, options, run_metadata,
        callable_runner, callable_runner_args, callable_options)
elif run_start_resp.action == OnRunStartAction.NON_DEBUG_RUN:
    # Invoke run() method of the wrapped session.
    if callable_runner:
        retvals = callable_runner(*callable_runner_args)
    elif callable_options:
        # pylint:disable=protected-access
        callable_object = self._sess._make_callable_from_options(
            callable_options)
        # pylint:enable=protected-access
        retvals = callable_object(*callable_runner_args)
    else:
        retvals = self._sess.run(
            fetches,
            feed_dict=feed_dict,
            options=options,
            run_metadata=run_metadata)

    # Prepare arg for the on-run-end callback.
    run_end_req = OnRunEndRequest(run_start_resp.action)
else:
    raise ValueError(
        "Invalid OnRunStartAction value: %s" % run_start_resp.action)

# Invoke on-run-end callback and obtain response.
run_end_resp = self.on_run_end(run_end_req)
_check_type(run_end_resp, OnRunEndResponse)
# Currently run_end_resp is only a placeholder. No action is taken on it.

exit(retvals)
