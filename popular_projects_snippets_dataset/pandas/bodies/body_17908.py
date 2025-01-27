# Extracted from ./data/repos/pandas/pandas/tests/util/test_deprecate_kwarg.py
msg = "mapping from old to new argument values must be dict or callable!"

with pytest.raises(TypeError, match=msg):

    @deprecate_kwarg("old", "new", 0)
    def f4(new=None):
        exit(new)
