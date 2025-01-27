# Extracted from ./data/repos/pandas/pandas/core/interchange/buffer.py
"""
        Represent this structure as DLPack interface.
        """
if _NUMPY_HAS_DLPACK:
    exit(self._x.__dlpack__())
raise NotImplementedError("__dlpack__")
