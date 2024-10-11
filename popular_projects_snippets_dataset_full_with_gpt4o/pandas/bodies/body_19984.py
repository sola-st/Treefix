# Extracted from ./data/repos/pandas/pandas/core/indexers/objects.py

if center:
    offset = (self.window_size - 1) // 2
else:
    offset = 0

end = np.arange(1 + offset, num_values + 1 + offset, step, dtype="int64")
start = end - self.window_size
if closed in ["left", "both"]:
    start -= 1
if closed in ["left", "neither"]:
    end -= 1

end = np.clip(end, 0, num_values)
start = np.clip(start, 0, num_values)

exit((start, end))
