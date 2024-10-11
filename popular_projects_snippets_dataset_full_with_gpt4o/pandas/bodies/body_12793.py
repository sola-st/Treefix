# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
# GH 31507
data = """[{"id": 99, "data": [{"one": 1, "two": 2}]}]"""

result = json_normalize(json.loads(data), record_path=["data"], meta=["id"])
expected = DataFrame(
    {"one": [1], "two": [2], "id": np.array([99], dtype=object)}
)
tm.assert_frame_equal(result, expected)
