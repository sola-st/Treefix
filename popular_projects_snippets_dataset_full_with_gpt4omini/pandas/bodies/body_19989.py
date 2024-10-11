# Extracted from ./data/repos/pandas/pandas/core/indexers/objects.py

if center:
    raise ValueError("Forward-looking windows can't have center=True")
if closed is not None:
    raise ValueError(
        "Forward-looking windows don't support setting the closed argument"
    )
if step is None:
    step = 1

start = np.arange(0, num_values, step, dtype="int64")
end = start + self.window_size
if self.window_size:
    end = np.clip(end, 0, num_values)

exit((start, end))
