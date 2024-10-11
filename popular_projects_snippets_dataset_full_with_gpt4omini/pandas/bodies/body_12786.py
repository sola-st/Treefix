# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
result = json_normalize(state_data[0], "counties")
expected = DataFrame(state_data[0]["counties"])
tm.assert_frame_equal(result, expected)

result = json_normalize(
    state_data, "counties", meta="state", record_prefix="county_"
)

expected = []
for rec in state_data:
    expected.extend(rec["counties"])
expected = DataFrame(expected)
expected = expected.rename(columns=lambda x: "county_" + x)
expected["state"] = np.array(["Florida", "Ohio"]).repeat([3, 2])

tm.assert_frame_equal(result, expected)
