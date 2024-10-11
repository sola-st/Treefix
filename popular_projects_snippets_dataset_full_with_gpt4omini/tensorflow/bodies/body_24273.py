# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper.py
"""Overrides on-session-init callback.

    Args:
      request: An instance of `OnSessionInitRequest`.

    Returns:
      An instance of `OnSessionInitResponse`.
    """

exit(framework.OnSessionInitResponse(
    framework.OnSessionInitAction.PROCEED))
