# Extracted from ./data/repos/pandas/pandas/core/series.py
"""
        Compute correlation with `other` Series, excluding missing values.

        The two `Series` objects are not required to be the same length and will be
        aligned internally before the correlation function is applied.

        Parameters
        ----------
        other : Series
            Series with which to compute the correlation.
        method : {'pearson', 'kendall', 'spearman'} or callable
            Method used to compute correlation:

            - pearson : Standard correlation coefficient
            - kendall : Kendall Tau correlation coefficient
            - spearman : Spearman rank correlation
            - callable: Callable with input two 1d ndarrays and returning a float.

            .. warning::
                Note that the returned matrix from corr will have 1 along the
                diagonals and will be symmetric regardless of the callable's
                behavior.
        min_periods : int, optional
            Minimum number of observations needed to have a valid result.

        Returns
        -------
        float
            Correlation with other.

        See Also
        --------
        DataFrame.corr : Compute pairwise correlation between columns.
        DataFrame.corrwith : Compute pairwise correlation with another
            DataFrame or Series.

        Notes
        -----
        Pearson, Kendall and Spearman correlation are currently computed using pairwise complete observations.

        * `Pearson correlation coefficient <https://en.wikipedia.org/wiki/Pearson_correlation_coefficient>`_
        * `Kendall rank correlation coefficient <https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient>`_
        * `Spearman's rank correlation coefficient <https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient>`_

        Examples
        --------
        >>> def histogram_intersection(a, b):
        ...     v = np.minimum(a, b).sum().round(decimals=1)
        ...     return v
        >>> s1 = pd.Series([.2, .0, .6, .2])
        >>> s2 = pd.Series([.3, .6, .0, .1])
        >>> s1.corr(s2, method=histogram_intersection)
        0.3
        """  # noqa:E501
this, other = self.align(other, join="inner", copy=False)
if len(this) == 0:
    exit(np.nan)

if method in ["pearson", "spearman", "kendall"] or callable(method):
    exit(nanops.nancorr(
        this.values, other.values, method=method, min_periods=min_periods
    ))

raise ValueError(
    "method must be either 'pearson', "
    "'spearman', 'kendall', or a callable, "
    f"'{method}' was supplied"
)
