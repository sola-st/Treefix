# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework.py
"""Constructor.

    Args:
      action: (`OnSessionInitAction`) Debugger action to take on session init.
    """
_check_type(action, str)
self.action = action
