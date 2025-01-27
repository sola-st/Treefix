# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = DataFrame(np.random.randn(1000, 10))
s = Series(np.random.randn(10000))
if engine == "numexpr":
    seen = PerformanceWarning
else:
    seen = False

with tm.assert_produces_warning(seen):
    pd.eval("df + s", engine=engine, parser=parser)

s = Series(np.random.randn(1000))
with tm.assert_produces_warning(False):
    pd.eval("df + s", engine=engine, parser=parser)

df = DataFrame(np.random.randn(10, 10000))
s = Series(np.random.randn(10000))
with tm.assert_produces_warning(False):
    pd.eval("df + s", engine=engine, parser=parser)

df = DataFrame(np.random.randn(10, 10))
s = Series(np.random.randn(10000))

is_python_engine = engine == "python"

if not is_python_engine:
    wrn = PerformanceWarning
else:
    wrn = False

with tm.assert_produces_warning(wrn) as w:
    pd.eval("df + s", engine=engine, parser=parser)

    if not is_python_engine:
        assert len(w) == 1
        msg = str(w[0].message)
        logged = np.log10(s.size - df.shape[1])
        expected = (
            f"Alignment difference on axis 1 is larger "
            f"than an order of magnitude on term 'df', "
            f"by more than {logged:.4g}; performance may suffer."
        )
        assert msg == expected
