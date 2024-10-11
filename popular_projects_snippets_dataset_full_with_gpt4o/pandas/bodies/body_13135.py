# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
if not _HAVE_FASTPARQUET:
    pytest.skip("fastparquet is not installed")
elif get_option("mode.data_manager") == "array":
    pytest.skip("ArrayManager is not supported with fastparquet")
exit("fastparquet")
