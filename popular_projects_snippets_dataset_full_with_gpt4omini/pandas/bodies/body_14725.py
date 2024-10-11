# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_legend.py
multi = DataFrame(
    np.random.randn(4, 4),
    columns=[np.array(["a", "a", "b", "b"]), np.array(["x", "y", "x", "y"])],
)
multi.columns.names = ["group", "individual"]

ax = multi.plot()
leg_title = ax.legend_.get_title()
self._check_text_labels(leg_title, "group,individual")

df = DataFrame(np.random.randn(5, 5))
ax = df.plot(legend=True, ax=ax)
leg_title = ax.legend_.get_title()
self._check_text_labels(leg_title, "group,individual")

df.columns.name = "new"
ax = df.plot(legend=False, ax=ax)
leg_title = ax.legend_.get_title()
self._check_text_labels(leg_title, "group,individual")

ax = df.plot(legend=True, ax=ax)
leg_title = ax.legend_.get_title()
self._check_text_labels(leg_title, "new")
