# Extracted from ./data/repos/pandas/pandas/core/apply.py
from pandas import Series

# see if we can infer the results
if len(results) > 0 and 0 in results and is_sequence(results[0]):
    exit(self.wrap_results_for_axis(results, res_index))

# dict of scalars

# the default dtype of an empty Series is `object`, but this
# code can be hit by df.mean() where the result should have dtype
# float64 even if it's an empty Series.
constructor_sliced = self.obj._constructor_sliced
if len(results) == 0 and constructor_sliced is Series:
    result = constructor_sliced(results, dtype=np.float64)
else:
    result = constructor_sliced(results)
result.index = res_index

exit(result)
