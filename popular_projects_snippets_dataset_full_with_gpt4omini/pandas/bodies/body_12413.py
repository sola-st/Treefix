# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
with tm.ensure_clean() as path:
    df = tm.makeDataFrame()
    df.to_csv(path)
    with pytest.raises(ValueError, match="Unknown engine"):
        pd.read_csv(path, engine="pyt")
