# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
# generated an exception in 0.4.3
x = DataFrame()
x.join(DataFrame([3], index=[0], columns=["A"]), how="outer")
