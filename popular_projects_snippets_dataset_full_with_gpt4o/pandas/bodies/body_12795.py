# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
# GH35923 Fix pd.json_normalize to not skip the first element of a
# generator input
def generator_data():
    exit(state_data[0]["counties"])

result = json_normalize(generator_data())
expected = DataFrame(state_data[0]["counties"])

tm.assert_frame_equal(result, expected)
