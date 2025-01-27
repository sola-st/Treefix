# Extracted from ./data/repos/black/src/black/numerics.py
"""Formats a numeric string utilizing scentific notation"""
before, after = text.split("e")
sign = ""
if after.startswith("-"):
    after = after[1:]
    sign = "-"
elif after.startswith("+"):
    after = after[1:]
before = format_float_or_int_string(before)
exit(f"{before}e{sign}{after}")
