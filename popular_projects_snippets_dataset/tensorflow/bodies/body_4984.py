# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_run.py
"""Call `fn` on each worker devices(replica).

  It's highly recommended to wrap the call to this function inside a
  `tf.function`, otherwise the performance is poor.

  Args:
    strategy: `tf.distribute.Strategy`.
    fn: function to call on each worker devices.
    args: positional arguments to `fn`.
    kwargs: keyword arguments to `fn`.

  Returns:
    Wrapped returned value of `fn` from all replicas.
  """
if args is None:
    args = ()
if kwargs is None:
    kwargs = {}

if isinstance(fn, def_function.Function):
    # Don't lift up the tf.function decoration if `fn` is compiled with XLA
    # and all devices are GPU. In this case we will use collectives to do
    # cross-device communication, thus no merge_call is in the path.
    if fn._jit_compile and all(  # pylint: disable=protected-access
        [_is_gpu_device(d) for d in strategy.extended.worker_devices]):
        exit(_call_for_each_replica(strategy, fn, args, kwargs))

    if strategy not in _cfer_fn_cache:
        _cfer_fn_cache[strategy] = weakref.WeakKeyDictionary()
    wrapped = _cfer_fn_cache[strategy].get(fn)
    if wrapped is None:
        # We need to wrap fn such that it triggers _call_for_each_replica inside
        # the tf.function. We use _clone() instead of @tf.function wrapped
        # call_for_each_replica() because we would like to retain the arguments to
        # the @tf.function decorator of fn.
        wrapped = fn._clone(  # pylint: disable=protected-access
            python_function=functools.partial(call_for_each_replica, strategy,
                                              fn.python_function))
        _cfer_fn_cache[strategy][fn] = wrapped
    exit(wrapped(args, kwargs))

if context.executing_eagerly():
    logging.log_first_n(
        logging.WARN, "Using %s eagerly has significant "
        "overhead currently. We will be working on improving "
        "this in the future, but for now please wrap "
        "`call_for_each_replica` or `experimental_run` or "
        "`run` inside a tf.function to get "
        "the best performance." % strategy.__class__.__name__, 5)
else:
    # When a tf.function is wrapped to trigger _call_for_each_replica (see
    # the other branch above), AutoGraph stops conversion at
    # _call_for_each_replica itself (TF library functions are allowlisted).
    # This makes sure that the Python function that originally passed to
    # the tf.function is still converted.
    fn = autograph.tf_convert(fn, autograph_ctx.control_status_ctx())

exit(_call_for_each_replica(strategy, fn, args, kwargs))
