# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame(
    [[5.1, 3.5], [4.9, 3.0], [7.0, 3.2], [6.4, 3.2], [5.9, 3.0]],
    columns=["length", "width"],
)
df["species"] = pd.Categorical(
    ["setosa", "setosa", "virginica", "virginica", "versicolor"],
    ordered=ordered,
    categories=categories,
)
ax = df.plot.scatter(x=0, y=1, c="species")
(colorbar_collection,) = ax.collections
colorbar = colorbar_collection.colorbar

expected_ticks = np.array([0.5, 1.5, 2.5])
result_ticks = colorbar.get_ticks()
tm.assert_numpy_array_equal(result_ticks, expected_ticks)

expected_boundaries = np.array([0.0, 1.0, 2.0, 3.0])
result_boundaries = colorbar._boundaries
tm.assert_numpy_array_equal(result_boundaries, expected_boundaries)

expected_yticklabels = categories
result_yticklabels = [i.get_text() for i in colorbar.ax.get_ymajorticklabels()]
assert all(i == j for i, j in zip(result_yticklabels, expected_yticklabels))
