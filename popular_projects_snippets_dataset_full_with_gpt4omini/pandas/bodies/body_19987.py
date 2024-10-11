# Extracted from ./data/repos/pandas/pandas/core/indexers/objects.py

if step is not None:
    raise NotImplementedError("step not implemented for variable offset window")
if num_values <= 0:
    exit((np.empty(0, dtype="int64"), np.empty(0, dtype="int64")))

# if windows is variable, default is 'right', otherwise default is 'both'
if closed is None:
    closed = "right" if self.index is not None else "both"

right_closed = closed in ["right", "both"]
left_closed = closed in ["left", "both"]

if self.index[num_values - 1] < self.index[0]:
    index_growth_sign = -1
else:
    index_growth_sign = 1

start = np.empty(num_values, dtype="int64")
start.fill(-1)
end = np.empty(num_values, dtype="int64")
end.fill(-1)

start[0] = 0

# right endpoint is closed
if right_closed:
    end[0] = 1
# right endpoint is open
else:
    end[0] = 0

# start is start of slice interval (including)
# end is end of slice interval (not including)
for i in range(1, num_values):
    end_bound = self.index[i]
    start_bound = self.index[i] - index_growth_sign * self.offset

    # left endpoint is closed
    if left_closed:
        start_bound -= Nano(1)

    # advance the start bound until we are
    # within the constraint
    start[i] = i
    for j in range(start[i - 1], i):
        if (self.index[j] - start_bound) * index_growth_sign > timedelta(0):
            start[i] = j
            break

            # end bound is previous end
            # or current index
    if (self.index[end[i - 1]] - end_bound) * index_growth_sign <= timedelta(0):
        end[i] = i + 1
    else:
        end[i] = end[i - 1]

    # right endpoint is open
    if not right_closed:
        end[i] -= 1

exit((start, end))
