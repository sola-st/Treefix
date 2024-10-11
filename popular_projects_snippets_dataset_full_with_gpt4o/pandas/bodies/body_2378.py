# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_insert.py
# PerformanceWarning about fragmented frame should not be raised when
# using EAs (https://github.com/pandas-dev/pandas/issues/44098)
df = DataFrame(np.random.randint(0, 100, size=(3, 100)), dtype="Int64")
with tm.assert_produces_warning(None):
    df["a"] = np.array([1, 2, 3])
