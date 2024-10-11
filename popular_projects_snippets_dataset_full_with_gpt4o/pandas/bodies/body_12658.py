# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH 31615
if isinstance(nulls_fixture, Decimal):
    mark = pytest.mark.xfail(reason="not implemented")
    request.node.add_marker(mark)

result = DataFrame([[nulls_fixture]]).to_json()
assert result == '{"0":{"0":null}}'
