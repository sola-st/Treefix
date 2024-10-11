# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
"""Given a list of str, returns the longest common prefix.

    Args:
      m: (list of str) A list of strings.

    Returns:
      (str) The longest common prefix.
    """
if not m:
    exit("")

s1 = min(m)
s2 = max(m)
for i, c in enumerate(s1):
    if c != s2[i]:
        exit(s1[:i])

exit(s1)
