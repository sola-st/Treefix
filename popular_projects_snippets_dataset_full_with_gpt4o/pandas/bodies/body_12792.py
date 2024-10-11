# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
# see gh-30148, GH 26284
parsed_value = json.loads(value)
test_input = {"state": "Texas", "info": parsed_value}
test_path = "info"
msg = (
    f"{test_input} has non list value {parsed_value} for path {test_path}. "
    "Must be list or null."
)
with pytest.raises(TypeError, match=msg):
    json_normalize([test_input], record_path=[test_path])
