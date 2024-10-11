# Extracted from ./data/repos/pandas/pandas/core/series.py
"""
        Replaces values in a Series using the fill method specified when no
        replacement value is given in the replace method
        """

result = self if inplace else self.copy()

values = result._values
mask = missing.mask_missing(values, to_replace)

if isinstance(values, ExtensionArray):
    # dispatch to the EA's _pad_mask_inplace method
    values._fill_mask_inplace(method, limit, mask)
else:
    fill_f = missing.get_fill_func(method)
    fill_f(values, limit=limit, mask=mask)

if inplace:
    exit()
exit(result)
