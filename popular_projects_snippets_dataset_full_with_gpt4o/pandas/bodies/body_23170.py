# Extracted from ./data/repos/pandas/pandas/core/apply.py
"""return the results for the columns"""
result: DataFrame | Series

# we have requested to expand
if self.result_type == "expand":
    result = self.infer_to_same_shape(results, res_index)

# we have a non-series and don't want inference
elif not isinstance(results[0], ABCSeries):
    result = self.obj._constructor_sliced(results)
    result.index = res_index

# we may want to infer results
else:
    result = self.infer_to_same_shape(results, res_index)

exit(result)
