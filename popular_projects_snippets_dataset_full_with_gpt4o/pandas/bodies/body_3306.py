# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_matmul.py
# GH#21581 exception message should reflect original shapes,
#  not transposed shapes
a = np.random.rand(10, 4)
b = np.random.rand(5, 3)

df = DataFrame(b)

msg = r"shapes \(10, 4\) and \(5, 3\) not aligned"
with pytest.raises(ValueError, match=msg):
    a @ df
with pytest.raises(ValueError, match=msg):
    a.tolist() @ df
