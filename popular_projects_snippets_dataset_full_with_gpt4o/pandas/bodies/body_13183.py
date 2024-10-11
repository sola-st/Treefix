# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
monkeypatch.setenv("HOME", "TestingUser")
monkeypatch.setenv("USERPROFILE", "TestingUser")
with pytest.raises(OSError, match=r".*TestingUser.*"):
    read_parquet("~/file.parquet")
with pytest.raises(OSError, match=r".*TestingUser.*"):
    df_compat.to_parquet("~/file.parquet")
