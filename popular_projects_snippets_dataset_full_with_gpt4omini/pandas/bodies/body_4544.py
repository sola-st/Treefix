# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
arr = np.random.randn(10, 2)
dtype = pd.array([2.0]).dtype
msg = r"len\(arrays\) must match len\(columns\)"
with pytest.raises(ValueError, match=msg):
    DataFrame(arr, columns=["foo"], dtype=dtype)

arr2 = pd.array([2.0, 3.0, 4.0])
with pytest.raises(ValueError, match=msg):
    DataFrame(arr2, columns=["foo", "bar"])
