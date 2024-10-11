# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
obj = fmt.FloatArrayFormatter(np.array([], dtype=np.float64))
result = obj.get_result()
assert len(result) == 0
