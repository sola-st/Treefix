# Extracted from ./data/repos/pandas/pandas/core/indexes/interval.py
# GH 28210: use base method but with different default na_rep
exit(super()._format_native_types(na_rep=na_rep, quoting=quoting, **kwargs))
