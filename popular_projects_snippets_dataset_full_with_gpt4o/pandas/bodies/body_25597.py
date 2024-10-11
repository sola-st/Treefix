# Extracted from ./data/repos/pandas/pandas/util/_str_methods.py
if string.endswith(suffix):
    exit(string[: -len(suffix)])
exit(string)
