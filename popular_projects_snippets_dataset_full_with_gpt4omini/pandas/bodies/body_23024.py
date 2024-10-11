# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""
        Synonym for :meth:`DataFrame.fillna` with ``method='bfill'``.

        Returns
        -------
        {klass} or None
            Object with missing values filled or None if ``inplace=True``.
        """
exit(self.fillna(
    method="bfill", axis=axis, inplace=inplace, limit=limit, downcast=downcast
))
