# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
# GH23843: Enhanced JSON normalize
test_input = [
    {
        "CreatedBy": {"Name": "User001"},
        "Lookup": [
            {
                "TextField": "Some text",
                "UserField": {"Id": "ID001", "Name": "Name001"},
            },
            {
                "TextField": "Some text",
                "UserField": {"Id": "ID001", "Name": "Name001"},
            },
        ],
        "Image": {"a": "b"},
        "tags": [
            {"foo": "something", "bar": "else"},
            {"foo": "something2", "bar": "else2"},
        ],
    }
]

result = json_normalize(
    test_input,
    record_path=["Lookup"],
    meta=[["CreatedBy"], ["Image"]],
    max_level=max_level,
)
expected_df = DataFrame(data=expected, columns=result.columns.values)
tm.assert_equal(expected_df, result)
