# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nth.py
df = DataFrame([range(5)], columns=[list("ABCDE")])
gb = df.groupby([5, 5, 5, 6, 6], axis=1)
result = {
    "call": lambda start, stop: gb.nth(slice(start, stop)),
    "index": lambda start, stop: gb.nth[start:stop],
}[method](start, stop)
expected = DataFrame([expected_values], columns=[expected_columns])
tm.assert_frame_equal(result, expected)
