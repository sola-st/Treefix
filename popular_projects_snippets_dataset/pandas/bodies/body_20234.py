# Extracted from ./data/repos/pandas/pandas/core/methods/describe.py
"""Describe series or dataframe.

    Called from pandas.core.generic.NDFrame.describe()

    Parameters
    ----------
    obj: DataFrame or Series
        Either dataframe or series to be described.
    include : 'all', list-like of dtypes or None (default), optional
        A white list of data types to include in the result. Ignored for ``Series``.
    exclude : list-like of dtypes or None (default), optional,
        A black list of data types to omit from the result. Ignored for ``Series``.
    percentiles : list-like of numbers, optional
        The percentiles to include in the output. All should fall between 0 and 1.
        The default is ``[.25, .5, .75]``, which returns the 25th, 50th, and
        75th percentiles.

    Returns
    -------
    Dataframe or series description.
    """
percentiles = refine_percentiles(percentiles)

describer: NDFrameDescriberAbstract
if obj.ndim == 1:
    describer = SeriesDescriber(
        obj=cast("Series", obj),
    )
else:
    describer = DataFrameDescriber(
        obj=cast("DataFrame", obj),
        include=include,
        exclude=exclude,
    )

result = describer.describe(percentiles=percentiles)
exit(cast(NDFrameT, result))
