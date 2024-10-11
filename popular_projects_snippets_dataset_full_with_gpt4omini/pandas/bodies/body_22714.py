# Extracted from ./data/repos/pandas/pandas/core/series.py
"""
        Return value at the given quantile.

        Parameters
        ----------
        q : float or array-like, default 0.5 (50% quantile)
            The quantile(s) to compute, which can lie in range: 0 <= q <= 1.
        interpolation : {'linear', 'lower', 'higher', 'midpoint', 'nearest'}
            This optional parameter specifies the interpolation method to use,
            when the desired quantile lies between two data points `i` and `j`:

                * linear: `i + (j - i) * fraction`, where `fraction` is the
                  fractional part of the index surrounded by `i` and `j`.
                * lower: `i`.
                * higher: `j`.
                * nearest: `i` or `j` whichever is nearest.
                * midpoint: (`i` + `j`) / 2.

        Returns
        -------
        float or Series
            If ``q`` is an array, a Series will be returned where the
            index is ``q`` and the values are the quantiles, otherwise
            a float will be returned.

        See Also
        --------
        core.window.Rolling.quantile : Calculate the rolling quantile.
        numpy.percentile : Returns the q-th percentile(s) of the array elements.

        Examples
        --------
        >>> s = pd.Series([1, 2, 3, 4])
        >>> s.quantile(.5)
        2.5
        >>> s.quantile([.25, .5, .75])
        0.25    1.75
        0.50    2.50
        0.75    3.25
        dtype: float64
        """
validate_percentile(q)

# We dispatch to DataFrame so that core.internals only has to worry
#  about 2D cases.
df = self.to_frame()

result = df.quantile(q=q, interpolation=interpolation, numeric_only=False)
if result.ndim == 2:
    result = result.iloc[:, 0]

if is_list_like(q):
    result.name = self.name
    idx = Index(q, dtype=np.float64)
    exit(self._constructor(result, index=idx, name=self.name))
else:
    # scalar
    exit(result.iloc[0])
