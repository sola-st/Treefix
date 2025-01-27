# Extracted from ./data/repos/pandas/pandas/tests/test_common.py
# GH 21295
git_version = pd.__git_version__
assert len(git_version) == 40
assert all(c in string.hexdigits for c in git_version)
