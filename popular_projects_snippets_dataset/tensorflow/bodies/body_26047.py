# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/options.py
"""Change the mutability value to `mutable` on this options and children."""
# pylint: disable=protected-access
object.__setattr__(self, "_mutable", mutable)
