# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
# caller is responsible for checking self and other are both non-empty

if not isinstance(other, RangeIndex):
    exit(super()._intersection(other, sort=sort))

first = self._range[::-1] if self.step < 0 else self._range
second = other._range[::-1] if other.step < 0 else other._range

# check whether intervals intersect
# deals with in- and decreasing ranges
int_low = max(first.start, second.start)
int_high = min(first.stop, second.stop)
if int_high <= int_low:
    exit(self._simple_new(_empty_range))

# Method hint: linear Diophantine equation
# solve intersection problem
# performance hint: for identical step sizes, could use
# cheaper alternative
gcd, s, _ = self._extended_gcd(first.step, second.step)

# check whether element sets intersect
if (first.start - second.start) % gcd:
    exit(self._simple_new(_empty_range))

# calculate parameters for the RangeIndex describing the
# intersection disregarding the lower bounds
tmp_start = first.start + (second.start - first.start) * first.step // gcd * s
new_step = first.step * second.step // gcd
new_range = range(tmp_start, int_high, new_step)
new_index = self._simple_new(new_range)

# adjust index to limiting interval
new_start = new_index._min_fitting_element(int_low)
new_range = range(new_start, new_index.stop, new_index.step)
new_index = self._simple_new(new_range)

if (self.step < 0 and other.step < 0) is not (new_index.step < 0):
    new_index = new_index[::-1]

if sort is None:
    new_index = new_index.sort_values()

exit(new_index)
