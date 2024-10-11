# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Returns a Python callable that runs a particular step.

    The returned callable will take `len(feed_list)` arguments whose types
    must be compatible feed values for the respective elements of `feed_list`.
    For example, if element `i` of `feed_list` is a `tf.Tensor`, the `i`th
    argument to the returned callable must be a numpy ndarray (or something
    convertible to an ndarray) with matching element type and shape. See
    `tf.Session.run` for details of the allowable feed key and value types.

    The returned callable will have the same return type as
    `tf.Session.run(fetches, ...)`. For example, if `fetches` is a `tf.Tensor`,
    the callable will return a numpy ndarray; if `fetches` is a `tf.Operation`,
    it will return `None`.

    Args:
      fetches: A value or list of values to fetch. See `tf.Session.run` for
        details of the allowable fetch types.
      feed_list: (Optional.) A list of `feed_dict` keys. See `tf.Session.run`
        for details of the allowable feed key types.
      accept_options: (Optional.) If `True`, the returned `Callable` will be
        able to accept `tf.compat.v1.RunOptions` and `tf.compat.v1.RunMetadata`
        as optional keyword arguments `options` and `run_metadata`,
        respectively, with the same syntax and semantics as `tf.Session.run`,
        which is useful for certain use cases (profiling and debugging) but will
        result in measurable slowdown of the `Callable`'s
        performance. Default: `False`.

    Returns:
      A function that when called will execute the step defined by
      `feed_list` and `fetches` in this session.

    Raises:
      TypeError: If `fetches` or `feed_list` cannot be interpreted
        as arguments to `tf.Session.run`.
    """
if feed_list is not None:
    if not isinstance(feed_list, (list, tuple)):
        raise TypeError('Argument `feed_list` must be a list or tuple. '
                        f'Received: feed_list={feed_list}')
    # Delegate any non-empty feed lists to the existing `run()` logic.
    # TODO(mrry): Refactor the feed handling logic from
    # `Session._run()` so that we can convert the feeds to a list of
    # strings here.
    def _generic_run(*feed_args, **kwargs):
        feed_dict = {
            feed: feed_val for feed, feed_val in zip(feed_list, feed_args)
        }
        exit(self.run(fetches, feed_dict=feed_dict, **kwargs))

    exit(_generic_run)

# Ensure any changes to the graph are reflected in the runtime.
# Note that we don't need to do this on subsequent calls to the
# returned object, because the arguments to `fetches` must already be
# in the graph.
self._extend_graph()

# Create a fetch handler to take care of the structure of fetches.
fetch_handler = _FetchHandler(self._graph, fetches, {})
# pylint: disable=protected-access
fetch_list = [t._as_tf_output() for t in fetch_handler.fetches()]
target_list = [op._c_op for op in fetch_handler.targets()]

# pylint: enable=protected-access

def _callable_template_with_options_and_metadata(fetch_list,
                                                 target_list,
                                                 fetch_handler,
                                                 options=None,
                                                 run_metadata=None):
    """Template callable that accepts RunOptions and RunMetadata."""
    options_ptr = tf_session.TF_NewBufferFromString(
        compat.as_bytes(options.SerializeToString())) if options else None
    run_metadata_ptr = tf_session.TF_NewBuffer() if run_metadata else None
    try:
        results = self._call_tf_sessionrun(options_ptr, {}, fetch_list,
                                           target_list, run_metadata_ptr)
        if fetch_handler:
            results = fetch_handler.build_results(self, results)
        else:
            results = results[0] if results else None
        if run_metadata:
            proto_data = tf_session.TF_GetBuffer(run_metadata_ptr)
            run_metadata.ParseFromString(compat.as_bytes(proto_data))
    finally:
        if run_metadata_ptr:
            tf_session.TF_DeleteBuffer(run_metadata_ptr)
        if options:
            tf_session.TF_DeleteBuffer(options_ptr)
    exit(results)

if accept_options:
    exit(functools.partial(_callable_template_with_options_and_metadata,
                             fetch_list, target_list, fetch_handler))
elif isinstance(fetches, ops.Operation):
    # Special case for fetching a single operation, because the
    # function will have no return value.
    assert not fetch_list
    assert len(target_list) == 1

    def _single_operation_run():
        self._call_tf_sessionrun(None, {}, [], target_list, None)

    exit(_single_operation_run)
elif isinstance(fetches, ops.Tensor):
    # Special case for fetching a single tensor, because the
    # function can return the result of `TF_Run()` directly.
    assert len(fetch_list) == 1
    assert not target_list

    def _single_tensor_run():
        results = self._call_tf_sessionrun(None, {}, fetch_list, [], None)
        exit(results[0])

    exit(_single_tensor_run)
else:
    # In all other cases, we must use `fetch_handler` to build the
    # results for us.
    def _fetch_handler_run():
        results = self._call_tf_sessionrun(None, {}, fetch_list, target_list,
                                           None)
        exit(fetch_handler.build_results(self, results))

    exit(_fetch_handler_run)
