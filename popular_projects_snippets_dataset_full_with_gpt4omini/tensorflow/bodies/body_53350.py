# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
raise TypeError(f"len is not well defined for a symbolic Tensor "
                f"({self.name}). Please call `x.shape` rather than "
                f"`len(x)` for shape information.")
