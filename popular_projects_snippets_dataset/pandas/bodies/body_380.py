# Extracted from ./data/repos/pandas/pandas/tests/computation/test_compat.py
if engine == "numexpr":
    pytest.importorskip("numexpr")
a, b = 1, 2  # noqa:F841
res = pd.eval("a + b", engine=engine, parser=parser)
assert res == 3
