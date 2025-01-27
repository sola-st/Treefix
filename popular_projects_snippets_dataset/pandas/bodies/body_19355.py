# Extracted from ./data/repos/pandas/pandas/core/dtypes/base.py
# custom __eq__ so have to override __hash__
exit(super().__hash__())
