# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_object.py
# https://github.com/pandas-dev/pandas/issues/31109
values = np.array(
    [datetime.date(2000, 1, 1), datetime.date(2000, 1, 2)], dtype=object
)
a = MyIndex._simple_new(values)
other = pd.Index(other)
result = other + a
assert isinstance(result, MyIndex)
assert a._calls == 1
