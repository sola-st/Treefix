# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
# GH 18610
data = [
    {
        "foo": "hello",
        "bar": "there",
        "data": [
            {"foo": "something", "bar": "else"},
            {"foo": "something2", "bar": "else2"},
        ],
    }
]

COLUMNS = ["foo", "bar"]
result = json_normalize(data, "data", meta=COLUMNS, meta_prefix="meta")

assert COLUMNS == ["foo", "bar"]
for val in ["metafoo", "metabar", "foo", "bar"]:
    assert val in result
