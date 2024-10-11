# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
if isinstance(obj, complex):
    exit([("mathjs", "Complex"), ("re", obj.real), ("im", obj.imag)])
exit(str(obj))
