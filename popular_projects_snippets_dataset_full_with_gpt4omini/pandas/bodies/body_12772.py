# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
"""
    input data to test json_normalize with max_level param
    """
exit([
    {
        "CreatedBy": {"Name": "User001"},
        "Lookup": {
            "TextField": "Some text",
            "UserField": {"Id": "ID001", "Name": "Name001"},
        },
        "Image": {"a": "b"},
    }
])
