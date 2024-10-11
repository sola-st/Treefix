# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
# GH41876
# Ensure errors='ignore' works as intended even when a record_path of length
# greater than one is passed in
result = json_normalize(
    data=missing_metadata,
    record_path=["previous_residences", "cities"],
    meta="name",
    errors="ignore",
)
ex_data = [
    ["Foo York City", "Alice"],
    ["Barmingham", np.nan],
]
columns = ["city_name", "name"]
expected = DataFrame(ex_data, columns=columns)
tm.assert_frame_equal(result, expected)
