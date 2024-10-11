# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_color.py
import matplotlib.pyplot as plt

random_array = np.random.random((1000, 3))
df = DataFrame(random_array, columns=["A label", "B label", "C label"])

fig, axes = plt.subplots(1, 2)
df.plot.scatter("A label", "B label", c="C label", ax=axes[0])
df.plot.scatter("A label", "B label", c="C label", ax=axes[1])
plt.tight_layout()

points = np.array([ax.get_position().get_points() for ax in fig.axes])
axes_x_coords = points[:, :, 0]
parent_distance = axes_x_coords[1, :] - axes_x_coords[0, :]
colorbar_distance = axes_x_coords[3, :] - axes_x_coords[2, :]
assert np.isclose(parent_distance, colorbar_distance, atol=1e-7).all()
