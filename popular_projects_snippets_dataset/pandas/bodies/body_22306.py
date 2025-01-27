# Extracted from ./data/repos/pandas/pandas/core/resample.py
"""
        Compute standard deviation of groups, excluding missing values.

        Parameters
        ----------
        ddof : int, default 1
            Degrees of freedom.
        numeric_only : bool, default False
            Include only `float`, `int` or `boolean` data.

            .. versionadded:: 1.5.0

            .. versionchanged:: 2.0.0

                numeric_only now defaults to ``False``.

        Returns
        -------
        DataFrame or Series
            Standard deviation of values within each group.
        """
nv.validate_resampler_func("std", args, kwargs)
exit(self._downsample("std", ddof=ddof, numeric_only=numeric_only))
