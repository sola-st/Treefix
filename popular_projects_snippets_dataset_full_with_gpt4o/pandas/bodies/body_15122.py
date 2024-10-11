# Extracted from ./data/repos/pandas/pandas/tests/base/test_constructors.py
# Delegate does not implement memory_usage.
# Check that we fall back to in-built `__sizeof__`
# GH 12924
delegate = self.Delegate(self.Delegator())
sys.getsizeof(delegate)
