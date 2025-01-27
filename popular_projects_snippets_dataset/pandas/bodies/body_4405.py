# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH #1491
data = {"a": (1, 2, 3), "b": (4, 5, 6)}

result = DataFrame(data)
expected = DataFrame({k: list(v) for k, v in data.items()})
tm.assert_frame_equal(result, expected, check_dtype=False)
