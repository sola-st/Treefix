# Extracted from ./data/repos/pandas/pandas/util/_decorators.py
"""Specify which version of pandas the deprecation will take place in."""
if version is None:
    exit("In a future version of pandas")
else:
    exit(f"Starting with pandas version {version}")
