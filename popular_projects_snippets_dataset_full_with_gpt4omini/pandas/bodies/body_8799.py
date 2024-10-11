# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
op_name = f"__{comparison_op.__name__}__"

a = pd.array(["a", None, "c"], dtype=dtype)
other = 42

if op_name not in ["__eq__", "__ne__"]:
    with pytest.raises(TypeError, match="not supported between"):
        getattr(a, op_name)(other)

    exit()

result = getattr(a, op_name)(other)
expected_data = {"__eq__": [False, None, False], "__ne__": [True, None, True]}[
    op_name
]
expected = pd.array(expected_data, dtype="boolean")
tm.assert_extension_array_equal(result, expected)
