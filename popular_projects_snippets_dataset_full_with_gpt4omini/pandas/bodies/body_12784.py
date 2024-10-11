# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
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

msg = r"Conflicting metadata name (foo|bar), need distinguishing prefix"
with pytest.raises(ValueError, match=msg):
    json_normalize(data, "data", meta=["foo", "bar"])

result = json_normalize(data, "data", meta=["foo", "bar"], meta_prefix="meta")

for val in ["metafoo", "metabar", "foo", "bar"]:
    assert val in result
