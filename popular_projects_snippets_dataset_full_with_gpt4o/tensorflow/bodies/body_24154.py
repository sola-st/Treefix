# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework.py
"""Constructor of NonInteractiveDebugWrapperSession.

    Args:
      sess: The TensorFlow `Session` object being wrapped.
      watch_fn: (`Callable`) A Callable that maps the fetches and feeds of a
        debugged `Session.run()` call to `WatchOptions.`
        * Args:
          * `fetches`: the fetches to the `Session.run()` call.
          * `feeds`: the feeds to the `Session.run()` call.

        * Returns:
         (`tf_debug.WatchOptions`) An object containing debug options including
           the debug ops to use, the node names, op types and/or tensor data
           types to watch, etc. See the documentation of `tf_debug.WatchOptions`
           for more details.
      thread_name_filter: Regular-expression white list for threads on which the
        wrapper session will be active. See doc of `BaseDebugWrapperSession` for
        more details.
      pass_through_operrors: If true, all captured OpErrors will be
        propagated.  By default this captures all OpErrors.
    Raises:
       TypeError: If a non-None `watch_fn` is specified and it is not callable.
    """

BaseDebugWrapperSession.__init__(
    self, sess, thread_name_filter=thread_name_filter,
    pass_through_operrors=pass_through_operrors)

self._watch_fn = None
if watch_fn is not None:
    if not callable(watch_fn):
        raise TypeError("watch_fn is not callable")
    self._watch_fn = watch_fn
