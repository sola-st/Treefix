# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
with pytest.raises(ValueError, match="expected type bool"):
    multiindex_df.reset_index(allow_duplicates=allow_duplicates)
