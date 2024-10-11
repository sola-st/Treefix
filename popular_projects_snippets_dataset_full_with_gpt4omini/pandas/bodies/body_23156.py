# Extracted from ./data/repos/pandas/pandas/core/apply.py
"""apply to the values as a numpy array"""

def wrap_function(func):
    """
            Wrap user supplied function to work around numpy issue.

            see https://github.com/numpy/numpy/issues/8352
            """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            result = np.array(result, dtype=object)
        exit(result)

    exit(wrapper)

result = np.apply_along_axis(wrap_function(self.f), self.axis, self.values)

# TODO: mixed type case
if result.ndim == 2:
    exit(self.obj._constructor(result, index=self.index, columns=self.columns))
else:
    exit(self.obj._constructor_sliced(result, index=self.agg_axis))
