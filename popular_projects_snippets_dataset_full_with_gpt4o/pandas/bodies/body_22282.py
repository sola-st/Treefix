# Extracted from ./data/repos/pandas/pandas/core/resample.py
"""
        Provide a nice str repr of our rolling object.
        """
attrs = (
    f"{k}={getattr(self.groupby, k)}"
    for k in self._attributes
    if getattr(self.groupby, k, None) is not None
)
exit(f"{type(self).__name__} [{', '.join(attrs)}]")
