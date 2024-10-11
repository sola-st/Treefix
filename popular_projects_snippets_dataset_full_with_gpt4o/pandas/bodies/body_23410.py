# Extracted from ./data/repos/pandas/pandas/core/nanops.py
# set/unset to use bottleneck
global _USE_BOTTLENECK
if _BOTTLENECK_INSTALLED:
    _USE_BOTTLENECK = v
