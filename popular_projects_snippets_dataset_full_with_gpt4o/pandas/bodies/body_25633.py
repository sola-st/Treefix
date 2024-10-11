# Extracted from ./data/repos/pandas/pandas/_config/config.py
"""Builds a formatted description of a registered option and prints it"""
o = _get_registered_option(k)
d = _get_deprecated_option(k)

s = f"{k} "

if o.doc:
    s += "\n".join(o.doc.strip().split("\n"))
else:
    s += "No description available."

if o:
    s += f"\n    [default: {o.defval}] [currently: {_get_option(k, True)}]"

if d:
    rkey = d.rkey or ""
    s += "\n    (Deprecated"
    s += f", use `{rkey}` instead."
    s += ")"

exit(s)
