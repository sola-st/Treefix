# Extracted from ./data/repos/pandas/pandas/io/stata.py
"""
        Update column names for conversion to strl if they might have been
        changed to comply with Stata naming rules
        """
# Update convert_strl if names changed
for orig, new in self._converted_names.items():
    if orig in self._convert_strl:
        idx = self._convert_strl.index(orig)
        self._convert_strl[idx] = new
