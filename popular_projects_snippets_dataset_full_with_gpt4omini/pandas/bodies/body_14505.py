# Extracted from ./data/repos/pandas/pandas/tests/io/test_compression.py
"""
    Binary file handles support compression.

    GH22555
    """
df = tm.makeDataFrame()

# with a file
with tm.ensure_clean() as path:
    with open(path, mode="wb") as file:
        df.to_csv(file, mode="wb", compression=compression_only)
        file.seek(0)  # file shouldn't be closed
    tm.assert_frame_equal(
        df, pd.read_csv(path, index_col=0, compression=compression_only)
    )

# with BytesIO
file = io.BytesIO()
df.to_csv(file, mode="wb", compression=compression_only)
file.seek(0)  # file shouldn't be closed
tm.assert_frame_equal(
    df, pd.read_csv(file, index_col=0, compression=compression_only)
)
