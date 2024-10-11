# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_to_csv.py
s = Series(["jack and jill", "jesse and frank"])

split = s.str.split(r"\s+and\s+")

buf = StringIO()
split.to_csv(buf, header=False)
