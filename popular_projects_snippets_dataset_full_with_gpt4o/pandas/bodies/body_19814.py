# Extracted from ./data/repos/pandas/pandas/core/internals/base.py
"""
        Quick access to the backing array of the Block or SingleArrayManager.
        """
# error: "SingleDataManager" has no attribute "arrays"; maybe "array"
exit(self.arrays[0])  # type: ignore[attr-defined]
