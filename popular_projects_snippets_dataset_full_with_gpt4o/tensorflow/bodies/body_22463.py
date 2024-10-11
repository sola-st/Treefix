# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
"""Initializes a `FeedFnHook`.

    Args:
      feed_fn: function that takes no arguments and returns `dict` of `Tensor`
        to feed.
    """
self.feed_fn = feed_fn
