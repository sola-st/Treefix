# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_dict.py
# GH 46751
# Tests we get back native types for all orient types
df = DataFrame(data)
result = df.to_dict(orient)
if orient == "dict":
    assertion_iterator = (
        (i, key, value)
        for key, index_value_map in result.items()
        for i, value in index_value_map.items()
    )
elif orient == "list":
    assertion_iterator = (
        (i, key, value)
        for key, values in result.items()
        for i, value in enumerate(values)
    )
elif orient in {"split", "tight"}:
    assertion_iterator = (
        (i, key, result["data"][i][j])
        for i in result["index"]
        for j, key in enumerate(result["columns"])
    )
elif orient == "records":
    assertion_iterator = (
        (i, key, value)
        for i, record in enumerate(result)
        for key, value in record.items()
    )
elif orient == "index":
    assertion_iterator = (
        (i, key, value)
        for i, record in result.items()
        for key, value in record.items()
    )

for i, key, value in assertion_iterator:
    assert value == data[key][i]
    assert type(value) is expected_types[key][i]
