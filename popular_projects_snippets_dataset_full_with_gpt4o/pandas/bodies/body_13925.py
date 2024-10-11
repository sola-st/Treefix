# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_info.py
frame = request.getfixturevalue(fixture_func_name)
buf = StringIO()
frame.info(buf=buf)
result = buf.getvalue().splitlines()
assert len(result) > 10
