# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# https://github.com/pandas-dev/pandas/issues/26551
df = pd.DataFrame({"a": list(range(0, 3))})
with tm.ensure_clean() as path:
    df.to_parquet(path, pa)
    result = read_parquet(
        path, pa, filters=[("a", "==", 0)], use_legacy_dataset=False
    )
assert len(result) == 1
