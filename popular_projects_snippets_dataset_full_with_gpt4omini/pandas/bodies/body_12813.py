# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_readlines.py
# GH33787
df = DataFrame(
    [([1, 2], ["2020-03-05", "2020-04-08T09:58:49+00:00"], "hector")],
    columns=["accounts", "date", "name"],
)
json_line = df.to_json(lines=True, orient="records")
result = read_json(json_line)
expected = DataFrame(
    [[1, "2020-03-05", "hector"], [2, "2020-04-08T09:58:49+00:00", "hector"]],
    columns=["accounts", "date", "name"],
)
tm.assert_frame_equal(result, expected)
