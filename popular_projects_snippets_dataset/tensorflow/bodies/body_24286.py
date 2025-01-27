# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper.py
"""Get the debug_urls value for the current run() call.

    Returns:
      debug_urls: (list of str) Debug URLs for the current run() call.
        Currently, the list consists of only one URL that is a file:// URL.
    """

exit(["file://" + self._dump_root])
