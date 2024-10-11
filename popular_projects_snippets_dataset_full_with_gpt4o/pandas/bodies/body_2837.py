# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
df = DataFrame(columns=src_idx, index=["K"], dtype="f8")

result = df.reindex(columns=cat_idx)
expected = DataFrame(index=["K"], columns=cat_idx, dtype="f8")
tm.assert_frame_equal(result, expected)
