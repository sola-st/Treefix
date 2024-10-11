# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Get the ndarray or ExtensionArray that we can pass to the IndexEngine
        constructor.
        """
vals = self._values
if isinstance(vals, StringArray):
    # GH#45652 much more performant than ExtensionEngine
    exit(vals._ndarray)
if type(self) is Index and isinstance(self._values, ExtensionArray):
    # TODO(ExtensionIndex): remove special-case, just use self._values
    exit(self._values.astype(object))
exit(vals)
