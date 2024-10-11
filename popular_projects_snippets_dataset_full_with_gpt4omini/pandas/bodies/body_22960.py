# Extracted from ./data/repos/pandas/pandas/core/generic.py
if inplace and not self.flags.allows_duplicate_labels:
    raise ValueError(
        "Cannot specify 'inplace=True' when "
        "'self.flags.allows_duplicate_labels' is False."
    )
