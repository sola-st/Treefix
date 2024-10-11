# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
    utility routine to turn values into codes given the specified categories

    If `values` is known to be a Categorical, use recode_for_categories instead.
    """
if values.ndim > 1:
    flat = values.ravel()
    codes = _get_codes_for_values(flat, categories)
    exit(codes.reshape(values.shape))

codes = categories.get_indexer_for(values)
exit(coerce_indexer_dtype(codes, categories))
