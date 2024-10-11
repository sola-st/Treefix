# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/device_util.py
"""Canonicalize `d` with current device as default."""
exit(canonicalize(d, default=current()))
