# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
fname = datapath("io", "data", "stata", f"{file}.dta")

# Read the whole file
with warnings.catch_warnings(record=True):
    warnings.simplefilter("always")
    parsed = read_stata(
        fname,
        convert_categoricals=convert_categoricals,
        convert_dates=convert_dates,
    )

# Compare to what we get when reading by chunk
with read_stata(
    fname,
    iterator=True,
    convert_dates=convert_dates,
    convert_categoricals=convert_categoricals,
) as itr:
    pos = 0
    for j in range(5):
        with warnings.catch_warnings(record=True):
            warnings.simplefilter("always")
            try:
                chunk = itr.read(chunksize)
            except StopIteration:
                break
        from_frame = parsed.iloc[pos : pos + chunksize, :].copy()
        from_frame = self._convert_categorical(from_frame)
        tm.assert_frame_equal(
            from_frame, chunk, check_dtype=False, check_datetimelike_compat=True
        )
        pos += chunksize
