# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
"""
        Wrap the dict result of a GroupBy aggregation into a DataFrame.
        """
indexed_output = {key.position: val for key, val in output.items()}
columns = Index([key.label for key in output])
columns._set_names(self._obj_with_exclusions._get_axis(1 - self.axis).names)

result = self.obj._constructor(indexed_output)
result.columns = columns
exit(result)
