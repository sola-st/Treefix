import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
import pandas.core.nanops as nanops # pragma: no cover

min_periods = 1 # pragma: no cover
ddof = 1 # pragma: no cover

import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/series.py
from l3.Runtime import _l_
"""
        Compute covariance with Series, excluding missing values.

        The two `Series` objects are not required to be the same length and
        will be aligned internally before the covariance is calculated.

        Parameters
        ----------
        other : Series
            Series with which to compute the covariance.
        min_periods : int, optional
            Minimum number of observations needed to have a valid result.
        ddof : int, default 1
            Delta degrees of freedom.  The divisor used in calculations
            is ``N - ddof``, where ``N`` represents the number of elements.

            .. versionadded:: 1.1.0

        Returns
        -------
        float
            Covariance between Series and other normalized by N-1
            (unbiased estimator).

        See Also
        --------
        DataFrame.cov : Compute pairwise covariance of columns.

        Examples
        --------
        >>> s1 = pd.Series([0.90010907, 0.13484424, 0.62036035])
        >>> s2 = pd.Series([0.12528585, 0.26962463, 0.51111198])
        >>> s1.cov(s2)
        -0.01685762652715874
        """
this, other = self.align(other, join="inner", copy=False)
_l_(10816)
if len(this) == 0:
    _l_(10818)

    aux = np.nan
    _l_(10817)
    exit(aux)
aux = nanops.nancov(
    this.values, other.values, min_periods=min_periods, ddof=ddof
)
_l_(10819)
exit(aux)
