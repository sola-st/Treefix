# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# GH 33173
np.random.seed(0)
df = DataFrame(dict(zip(["A", "B"], np.random.randn(2, 100))))

ax1 = _check_plot_works(df.plot, kind="hist", weights=weights)
ax2 = _check_plot_works(df.plot, kind="hist")

patch_height_with_weights = [patch.get_height() for patch in ax1.patches]

# original heights with no weights, and we manually multiply with example
# weights, so after multiplication, they should be almost same
expected_patch_height = [0.1 * patch.get_height() for patch in ax2.patches]

tm.assert_almost_equal(patch_height_with_weights, expected_patch_height)
