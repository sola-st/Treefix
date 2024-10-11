# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# for the case of Index, where the repr is traditional rather than
# stylized
idx = Index(["a", "b"])
res = eval("pd." + repr(idx))
tm.assert_series_equal(Series(res), Series(idx))
