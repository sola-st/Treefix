# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
target, source = target_source
result = target.join(source["MergedA"], on="C")
expected = target.join(source[["MergedA"]], on="C")
tm.assert_frame_equal(result, expected)
