# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
data = ["a", "b", "c"]
if kind is pd.Categorical:
    arr = pd.Series(kind(data, ordered=ordered), name="cats")
elif kind is pd.CategoricalIndex:
    arr = kind(data, ordered=ordered, name="cats")

result = convert_pandas_type_to_json_field(arr)
expected = {
    "name": "cats",
    "type": "any",
    "constraints": {"enum": data},
    "ordered": ordered,
}
assert result == expected
