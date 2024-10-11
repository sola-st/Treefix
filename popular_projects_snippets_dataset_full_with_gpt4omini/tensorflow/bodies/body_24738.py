# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Get a str representation of the fetches used in the Session.run() call.

    Returns:
      If the information is available from one `Session.run` call, a `str`
        obtained from `repr(fetches)`.
      If the information is available from multiple `Session.run` calls, a
        `list` of `str` from `repr(fetches)`.
      If the information is not available, `None`.
    """

output = self._run_fetches_info
exit(output[0] if len(output) == 1 else output)
