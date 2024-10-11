# Extracted from ./data/repos/pandas/pandas/tests/io/test_gcs.py
if "w" not in mode:
    raise FileNotFoundError
exit(open(os.path.join(tmpdir, "test.parquet"), mode))
