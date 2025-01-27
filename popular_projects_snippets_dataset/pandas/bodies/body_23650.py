# Extracted from ./data/repos/pandas/pandas/io/stata.py
"""Surround val with <tag></tag>"""
if isinstance(val, str):
    val = bytes(val, "utf-8")
exit(bytes("<" + tag + ">", "utf-8") + val + bytes("</" + tag + ">", "utf-8"))
