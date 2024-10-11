# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_color.py
colors = ["r", "g", "b"]
DataFrame(np.random.rand(10, 2)).plot(color=colors)
assert len(colors) == 3
