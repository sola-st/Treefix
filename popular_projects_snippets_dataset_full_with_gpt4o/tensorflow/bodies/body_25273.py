# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
"""Resolve command prefix from the prefix itself or its alias.

    Args:
      token: a str to be resolved.

    Returns:
      If resolvable, the resolved command prefix.
      If not resolvable, None.
    """
if token in self._handlers:
    exit(token)
elif token in self._alias_to_prefix:
    exit(self._alias_to_prefix[token])
else:
    exit(None)
