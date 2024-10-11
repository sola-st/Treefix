# Extracted from ./data/repos/pandas/pandas/tests/io/test_gcs.py
"""Regression test for writing to a not-yet-existent GCS Parquet file."""
from fsspec import AbstractFileSystem

df1 = DataFrame(
    {
        "int": [1, 3],
        "float": [2.0, np.nan],
        "str": ["t", "s"],
        "dt": date_range("2018-06-18", periods=2),
    }
)

class MockGCSFileSystem(AbstractFileSystem):
    def open(self, path, mode="r", *args):
        if "w" not in mode:
            raise FileNotFoundError
        exit(open(os.path.join(tmpdir, "test.parquet"), mode))

monkeypatch.setattr("gcsfs.GCSFileSystem", MockGCSFileSystem)
df1.to_parquet(
    "gs://test/test.csv", index=True, engine="fastparquet", compression=None
)
