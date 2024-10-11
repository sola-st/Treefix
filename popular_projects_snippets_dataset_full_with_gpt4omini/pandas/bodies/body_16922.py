# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append.py
mixed_frame = float_frame.copy()
mixed_frame["foo"] = "bar"

begin_index = float_frame.index[:5]
end_index = float_frame.index[5:]

begin_frame = float_frame.reindex(begin_index)
end_frame = float_frame.reindex(end_index)

appended = begin_frame._append(end_frame)
tm.assert_almost_equal(appended["A"], float_frame["A"])

del end_frame["A"]
partial_appended = begin_frame._append(end_frame, sort=sort)
assert "A" in partial_appended

partial_appended = end_frame._append(begin_frame, sort=sort)
assert "A" in partial_appended

# mixed type handling
appended = mixed_frame[:5]._append(mixed_frame[5:])
tm.assert_frame_equal(appended, mixed_frame)

# what to test here
mixed_appended = mixed_frame[:5]._append(float_frame[5:], sort=sort)
mixed_appended2 = float_frame[:5]._append(mixed_frame[5:], sort=sort)

# all equal except 'foo' column
tm.assert_frame_equal(
    mixed_appended.reindex(columns=["A", "B", "C", "D"]),
    mixed_appended2.reindex(columns=["A", "B", "C", "D"]),
)
