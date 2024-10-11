# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_generic.py
# GH 38588
assert (
    abctype in (e for e, _ in self.abc_pairs) or abctype in self.abc_subclasses
)
