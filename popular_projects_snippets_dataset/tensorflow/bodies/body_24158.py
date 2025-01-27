# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework.py
"""Get the debug_urls, and node/op allowlists for the current run() call.

    Args:
      fetches: Same as the `fetches` argument to `Session.run()`.
      feed_dict: Same as the `feed_dict argument` to `Session.run()`.

    Returns:
      debug_urls: (str or list of str) Debug URLs for the current run() call.
        Currently, the list consists of only one URL that is a file:// URL.
      watch_options: (WatchOptions) The return value of a watch_fn, containing
        options including debug_ops, and allowlists.
    """

debug_urls = self.prepare_run_debug_urls(fetches, feed_dict)
if self._watch_fn is None:
    watch_options = WatchOptions()
else:
    watch_options = self._watch_fn(fetches, feed_dict)
    if isinstance(watch_options, tuple):
        # For legacy return type (tuples).
        watch_options = WatchOptions(*watch_options)

exit((debug_urls, watch_options))
