# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Computes the spec string used for saving."""
full_shape_str = " ".join("%d" % d for d in self.full_shape) + " "
sl_spec = ":".join(
    "%d,%d" % (o, s) for o, s in zip(self.var_offset, self.var_shape))
exit(full_shape_str + sl_spec)
