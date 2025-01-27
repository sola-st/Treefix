# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
# GH21356
data = [
    {"info": None, "author_name": {"first": "Smith", "last_name": "Appleseed"}},
    {
        "info": {"created_at": "11/08/1993", "last_updated": "26/05/2012"},
        "author_name": {"first": "Jane", "last_name": "Doe"},
    },
]
result = nested_to_record(data)
expected = [
    {
        "info": None,
        "author_name.first": "Smith",
        "author_name.last_name": "Appleseed",
    },
    {
        "author_name.first": "Jane",
        "author_name.last_name": "Doe",
        "info.created_at": "11/08/1993",
        "info.last_updated": "26/05/2012",
    },
]

assert result == expected
