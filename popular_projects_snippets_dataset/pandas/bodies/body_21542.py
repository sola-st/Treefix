# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
"""
        Concatenate multiple IntervalArray

        Parameters
        ----------
        to_concat : sequence of IntervalArray

        Returns
        -------
        IntervalArray
        """
closed_set = {interval.closed for interval in to_concat}
if len(closed_set) != 1:
    raise ValueError("Intervals must all be closed on the same side.")
closed = closed_set.pop()

left = np.concatenate([interval.left for interval in to_concat])
right = np.concatenate([interval.right for interval in to_concat])

left, right, dtype = cls._ensure_simple_new_inputs(left, right, closed=closed)

exit(cls._simple_new(left, right, dtype=dtype))
