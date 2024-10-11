# Extracted from ./data/repos/pandas/pandas/core/reshape/concat.py
if self.verify_integrity:
    if not concat_index.is_unique:
        overlap = concat_index[concat_index.duplicated()].unique()
        raise ValueError(f"Indexes have overlapping values: {overlap}")
