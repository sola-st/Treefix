# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH 12004
df = DataFrame([["foo", "bar"], ["baz", "qux"]], columns=["a", "b"])

result = df.to_json(indent=indent)
spaces = " " * indent
expected = f"""{{
{spaces}"a":{{
{spaces}{spaces}"0":"foo",
{spaces}{spaces}"1":"baz"
{spaces}}},
{spaces}"b":{{
{spaces}{spaces}"0":"bar",
{spaces}{spaces}"1":"qux"
{spaces}}}
}}"""

assert result == expected
