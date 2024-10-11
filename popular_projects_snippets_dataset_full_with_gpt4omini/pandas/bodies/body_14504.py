# Extracted from ./data/repos/pandas/pandas/tests/io/test_compression.py
# Assert that passing a file object to to_csv while explicitly specifying a
# compression protocol triggers a RuntimeWarning, as per GH21227.
df = pd.DataFrame(
    100 * [[0.123456, 0.234567, 0.567567], [12.32112, 123123.2, 321321.2]],
    columns=["X", "Y", "Z"],
)
with tm.ensure_clean() as path:
    with icom.get_handle(path, "w", compression=compression_only) as handles:
        with tm.assert_produces_warning(RuntimeWarning):
            df.to_csv(handles.handle, compression=compression_only)
