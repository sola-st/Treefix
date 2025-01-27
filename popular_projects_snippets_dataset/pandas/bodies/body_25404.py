# Extracted from ./data/repos/pandas/pandas/_version.py
"""Return a + if we don't already have one, else return a ."""
if "+" in pieces.get("closest-tag", ""):
    exit(".")
exit("+")
