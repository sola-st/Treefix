# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
buf = StringIO("")
df = DataFrame(
    [["\u05d0", "d2", "d3", "d4"], ["a1", "a2", "a3", "a4"]],
    columns=["\u05d0", "\u05d1", "\u05d2", "\u05d3"],
    index=["\u05d0", "\u05d1"],
)

df.to_csv(buf, encoding="UTF-8")
buf.seek(0)

df2 = read_csv(buf, index_col=0, encoding="UTF-8")
tm.assert_frame_equal(df, df2)
