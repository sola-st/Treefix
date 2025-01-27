# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# see gh-14881
values = np.array([2**64 - i for i in range(1, 10)], dtype=np.uint64)

result = DataFrame({"a": values})
assert result["a"].dtype == np.uint64

# see gh-2355
data_scores = [
    (6311132704823138710, 273),
    (2685045978526272070, 23),
    (8921811264899370420, 45),
    (17019687244989530680, 270),
    (9930107427299601010, 273),
]
dtype = [("uid", "u8"), ("score", "u8")]
data = np.zeros((len(data_scores),), dtype=dtype)
data[:] = data_scores
df_crawls = DataFrame(data)
assert df_crawls["uid"].dtype == np.uint64
