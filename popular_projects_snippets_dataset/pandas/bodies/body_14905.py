# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
# GH9536
s = Series(np.arange(10), name="x")
err = np.random.rand(2, 10)

ax = s.plot(yerr=err, xerr=err)

result = np.vstack([i.vertices[:, 1] for i in ax.collections[1].get_paths()])
expected = (err.T * np.array([-1, 1])) + s.to_numpy().reshape(-1, 1)
tm.assert_numpy_array_equal(result, expected)

msg = (
    "Asymmetrical error bars should be provided "
    f"with the shape \\(2, {len(s)}\\)"
)
with pytest.raises(ValueError, match=msg):
    s.plot(yerr=np.random.rand(2, 11))

tm.close()
