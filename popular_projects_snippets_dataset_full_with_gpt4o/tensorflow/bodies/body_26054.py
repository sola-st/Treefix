# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/options.py
"""Change the mutability value to `mutable` on this options and children."""
# pylint: disable=protected-access
object.__setattr__(self, "_mutable", mutable)
self.autotune._set_mutable(mutable)
self.experimental_distribute._set_mutable(mutable)
self.experimental_optimization._set_mutable(mutable)
self.threading._set_mutable(mutable)
