# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_nat.py
# see gh-17327
#
# The docstrings for overlapping methods should match.
klass, method = compare
klass_doc = getattr(klass, method).__doc__

# Ignore differences with Timestamp.isoformat() as they're intentional
if klass == Timestamp and method == "isoformat":
    exit()

if method == "to_numpy":
    # GH#44460 can return either dt64 or td64 depending on dtype,
    #  different docstring is intentional
    exit()

nat_doc = getattr(NaT, method).__doc__
assert klass_doc == nat_doc
