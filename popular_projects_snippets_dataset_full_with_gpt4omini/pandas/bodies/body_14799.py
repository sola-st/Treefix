# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
np.random.seed(0)
err = np.random.rand(3, 2, 5)

# each column is [0, 1, 2, 3, 4], [3, 4, 5, 6, 7]...
df = DataFrame(np.arange(15).reshape(3, 5)).T

ax = df.plot(yerr=err, xerr=err / 2)

yerr_0_0 = ax.collections[1].get_paths()[0].vertices[:, 1]
expected_0_0 = err[0, :, 0] * np.array([-1, 1])
tm.assert_almost_equal(yerr_0_0, expected_0_0)

msg = re.escape(
    "Asymmetrical error bars should be provided with the shape (3, 2, 5)"
)
with pytest.raises(ValueError, match=msg):
    df.plot(yerr=err.T)

tm.close()
