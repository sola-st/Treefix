# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# GH 15289
df = DataFrame(mix_abc)
tm.assert_frame_equal(df, df.replace({}))
tm.assert_frame_equal(df, df.replace(Series([], dtype=object)))

tm.assert_frame_equal(df, df.replace({"b": {}}))
tm.assert_frame_equal(df, df.replace(Series({"b": {}})))
