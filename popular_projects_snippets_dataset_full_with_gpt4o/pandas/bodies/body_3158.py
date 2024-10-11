# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py

df = DataFrame(
    [[0.123456, 0.234567, 0.567567], [12.32112, 123123.2, 321321.2]],
    index=["A", "B"],
    columns=["X", "Y", "Z"],
)

with tm.ensure_clean() as filename:

    df.to_csv(filename, float_format="%.2f")

    rs = read_csv(filename, index_col=0)
    xp = DataFrame(
        [[0.12, 0.23, 0.57], [12.32, 123123.20, 321321.20]],
        index=["A", "B"],
        columns=["X", "Y", "Z"],
    )
    tm.assert_frame_equal(rs, xp)
