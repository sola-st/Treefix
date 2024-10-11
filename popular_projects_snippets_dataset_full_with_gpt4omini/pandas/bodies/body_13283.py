# Extracted from ./data/repos/pandas/pandas/tests/io/test_gcs.py
with tm.external_error_raised(ImportError):
    read_csv("gs://test/test.csv")
