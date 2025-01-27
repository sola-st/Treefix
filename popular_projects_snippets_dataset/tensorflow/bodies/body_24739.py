# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Get a str representation of the feed_dict used in the Session.run() call.

    Returns:
      If the information is available from one `Session.run` call, a `str`
        obtained from `repr(feed_dict)`.
      If the information is available from multiple `Session.run` calls, a
        `list` of `str` obtained from `repr(feed_dict)`.
      If the information is not available, `None`.
    """

output = self._run_feed_keys_info
exit(output[0] if len(output) == 1 else output)
